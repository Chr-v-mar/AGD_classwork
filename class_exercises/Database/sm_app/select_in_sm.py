import sqlite3

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None

    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")

select_users = "SELECT * from users"
select_posts = "SELECT * FROM posts"
select_users_posts = """
SELECT
    users.id,
    users.name,
    posts.description
FROM
    posts
    INNER JOIN users ON users.id = posts.user_id
"""
select_posts_comments_users = """
SELECT
    posts.description as post,
    comments.COMMENT as comment,
    users.name
FROM
    posts
    INNER JOIN comments ON posts.id = comments.post_id
    INNER JOIN users ON users.id = comments.user_id
"""

with (sqlite3.connect("sm_app.sqlite") as conn):
    users = execute_read_query(conn, select_users)
    posts = execute_read_query(conn, select_posts)
    users_posts = execute_read_query(conn, select_users_posts)
    posts_comments_users = execute_read_query(conn, select_posts_comments_users)

for user in users:
    print(user)
print(" ")
for post in posts:
    print(post)
print(" ")
for users_post in users_posts:
    print(users_post)
print(" ")
for posts_comments_user in posts_comments_users:
    print(posts_comments_user)