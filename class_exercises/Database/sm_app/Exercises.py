import sqlite3


select_question_comments = """
SELECT * FROM comments where COMMENT like "%?"
"""
rewrite_name_eliz = """
UPDATE users
SET name = "Lizzy"
WHERE name = "Elizabeth"
"""

select_user_and_postcount = """
SELECT name, COUNT(*) AS posts
FROM users
"""

select_user_and_comments = """
SELECT name, COUNT(*) AS comments
FROM users
"""



with (sqlite3.connect("sm_app.sqlite") as conn):
    cursor = conn.cursor()
    print(cursor.execute(select_question_comments))
    print(cursor.execute(rewrite_name_eliz))
    print(cursor.execute(select_user_and_postcount))
    print(cursor.execute(select_user_and_comments))
