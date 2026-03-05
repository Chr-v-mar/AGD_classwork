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
        user_information = []
        with so.Session(bind=self.engine) as session:
            user_names = session.scalars(sa.select(models.User.name).order_by(models.User.name)).all()
            for user in user_names:
                user_information.append(user.name)

        return user_information

    def add_new_user(self, name: str, age: int, gender: str, nationality: str) -> None:
        with so.Session(bind=self.engine) as session:
            add_user = models.User(name=name, age=age, gender=gender, nationality=nationality)
            session.add(add_user)
            session.commit()

    def get_user_posts(self):
        post_information = []
        with so.Session(bind=self.engine) as session:
            posts = session.scalars(sa.select(models.Post).where(models.Post.user_id == self.current_user_id)).all()
            for post in posts:
                post_information.append({'title': post.title,
                                         'content': post.description,
                                         'likes': post.number_of_likes})
        return post_information

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
        comments_information = []
        with so.Session(bind=self.engine) as session:
            comments = session.scalars(sa.select(models.Comment).where(models.Comment.user_id == self.current_user_id)).all()
            for comm in comments:
                comments_information.append({'comment': comm.comment})
        return comments_information

    def get_comments(self):
        comments_information = []
        with so.Session(bind=self.engine) as session:
            comments = session.scalars(sa.select(models.Comment).order_by(models.Comment.id)).all()
            for commente in comments:
                comments_information.append({'comment': commente.comment})
        return comments_information

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

    def like_post_toggle(self, post_id: int) -> None:
        with so.Session(bind=self.engine) as session:
            current_user = session.query(models.User).get(self.current_user_id)
            if current_user not in models.Post.liked_by_users:
                models.Post.liked_by_users.append(current_user)
            else:
                models.Post.liked_by_users.remove(current_user)
            session.commit()

    def like_comment_toggle(self, comment_id: int) -> None:
        with so.Session(bind=self.engine) as session:
            current_user = self.get_user_name(self.current_user_id)
            if current_user not in models.Comment.liked_by_users:
                models.Comment.liked_by_users.append(current_user)
            else:
                models.Comment.liked_by_users.remove(current_user)
            session.commit()

    #def delete_post(self, post_id: int) -> None:
        #with so.Session(bind=self.engine) as session:






if __name__ == '__main__':
    controller = Controller()
    controller.set_current_user_from_name('Alice')