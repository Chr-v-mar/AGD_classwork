from typing import Any

import sqlalchemy as sa
import sqlalchemy.orm as so

import models


class Controller:
    def __init__(self, db_location = 'sqlite:///social_media.db'):
        self.current_user_id: int|None = None
        self.viewing_post_user_id: int|None = None
        self.engine = sa.create_engine(db_location)

    def set_current_user_from_name(self, name:str) -> models.User | None:
        with so.Session(bind=self.engine) as session:
            user = session.scalars(sa.select(models.User).where(models.User.name == name)).one_or_none()

            if user is None:
                # Fallback behaviour: clear current user and return None
                self.current_user_id = None
                return None

            self.current_user_id = user.id
        return user

    def get_user_name(self, user_id: int|None = None) -> 'str':
        if user_id is None:
            user_id = self.current_user_id
        with so.Session(bind=self.engine) as session:
            name = session.get(models.User, user_id).name
        return name

    def get_user_names(self) -> list[str]:
        with so.Session(bind=self.engine) as session:
            user_names = session.scalars(sa.select(models.User.name).order_by(models.User.name)).all()
        return list(user_names)

    def add_new_user(self, name: str, age: int, gender: str, nationality: str) -> None:
        with so.Session(bind=self.engine) as session:
            add_user = models.User(name=name, age=age, gender=gender, nationality=nationality)
            session.add(add_user)
            session.commit()

    def get_user_posts(self):
        with so.Session(bind=self.engine) as session:
            posts = session.scalars(sa.select(models.Post).where(models.Post.user_id == self.current_user_id)).all()
        return list(posts)

    def get_posts(self):
        post_information = []
        with so.Session(bind=self.engine) as session:
            posts = session.scalars(sa.select(models.Post).order_by(models.Post.id)).all()
            for post in posts:
                post_information.append({'title': post.title,
                                         'content': post.description,
                                         'likes': post.number_of_likes})


        return post_information

    def get_user_comments(self):
        with so.Session(bind=self.engine) as session:
            comments = session.scalars(sa.select(models.Comment).where(models.Comment.user_id == self.current_user_id)).all()
        return list(comments)

    def get_comments(self):
        with so.Session(bind=self.engine) as session:
            comments = session.scalars(sa.select(models.Comment).order_by(models.Comment.id)).all()
        return list(comments)

    def post_a_post(self,  name: str, text: str, user: int) -> None:
        with so.Session(bind=self.engine) as session:
            postpost = models.Post(title= name, description=text, user_id= user)
            session.add(postpost)
            session.commit()

    def post_a_comment(self, text: str, user: int, post: int) -> None:
        with so.Session(bind=self.engine) as session:
            postcomment = models.Comment(comment=text, user_id=user, post_id=post)
            session.add(postcomment)
            session.commit()




if __name__ == '__main__':
    controller = Controller()
    controller.set_current_user_from_name('Alice')