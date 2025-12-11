import sqlite3


conn = sqlite3.connect('student.sqlite')
cursor = conn.cursor()
update_query = """
UPDATE students
SET last_name = ?
WHERE id = 4;
"""
cursor.execute(update_query, ('Smith',))
conn.commit()

increment_age_query = """
UPDATE students
SET age = age + 1;
"""
cursor.execute(increment_age_query)
conn.commit()
conn.close()
