import sqlite3
conn = sqlite3.connect('student.sqlite')
cursor = conn.cursor()
parameterised_insert_query = """
INSERT INTO students (first_name, last_name, age, gender)
    VALUES (?,?,?,?)
"""
cursor.execute(parameterised_insert_query, ("Aadit","Lamba", 16, "Male"))
conn.commit()
conn.close()