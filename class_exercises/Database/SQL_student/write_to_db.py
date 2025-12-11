import sqlite3
from faker import Faker
import random

fake = Faker('en_GB')

conn = sqlite3.connect('student.sqlite')
cursor = conn.cursor()
parameterised_insert_query = """
INSERT INTO students (first_name, last_name, age, gender)
    VALUES (?,?,?,?)
"""
fake.random.seed(4321)
random.seed(4321)
for _ in range(10):
    gender = random.choice(['Male', 'Female'])
    if gender == 'Male':
        first_name = fake.first_name_male()
        last_name = fake.last_name_male()
    else:
        first_name = fake.first_name_female()
        last_name = fake.last_name_female()
    age = random.randint(11,18)
    cursor.execute(parameterised_insert_query, (first_name, last_name, age, gender))

conn.commit()


conn.close()

