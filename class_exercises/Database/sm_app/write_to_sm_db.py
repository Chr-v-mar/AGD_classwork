import sqlite3

data = [('James', 25, 'male', 'USA'),
        ('Leila', 32, 'female', 'France'),
        ('Brigitte', 35, 'female', 'England'),
        ('Mike', 40, 'male', 'Denmark'),
        ('Elizabeth', 21, 'female', 'Canada'),
]

post_data = [('Happy', 'I am feeling very happy today', 1),
             ('Hot Weather', 'The weather is very hot today', 2),
             ('Help', 'I need some help with my work', 2),
             ('Great News', 'I am getting married', 1),
             ('Interesting Game', 'It was a fantastic game of tennis', 5),
             ('Party', 'Anyone up for a late-night party today?', 3),
]

comment_data = [('Count me in', 1, 6),
                ('What sort of help?', 5, 3),
                ('Congrats buddy', 2, 4),
                ('I was rooting for Nadal though', 4, 5),
                ('Help with your thesis?', 2, 3),
                ('Many congratulations', 5, 4),
]
conn = sqlite3.connect('sm_app.sqlite')
cursor = conn.cursor()

parameterised_write_query = """
INSERT INTO users(name, age, gender, nationality)
    VALUES(?, ?, ?, ?)
"""
#cursor.executemany(parameterised_write_query, data)

parameterised_insert_query = """
INSERT INTO posts(title, description, user_id)
    VALUES(?, ?, ?)
"""

#cursor.execute(parameterised_insert_query, ("Happy", "I am feeling very happy today", 1))
#cursor.executemany(parameterised_insert_query, post_data)

parameterised_comment_query = """
INSERT INTO comments(COMMENT, user_id,post_id)
    VALUES(?, ?, ?)
"""
cursor.executemany(parameterised_comment_query, comment_data)

conn.commit()
