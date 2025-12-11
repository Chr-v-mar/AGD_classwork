# Connect the database to Python using the sqlite3 module
import sqlite3

# Example of getting employee data from a database
# Connect to the database
conn = sqlite3.connect("chinook.db")
# A cursor is a pointer to a place in the database which allows access
# to a table row-by-row
cursor = conn.cursor()
# This is the SQL query
query = "SELECT FirstName, LastName, Title FROM employees;"
# The cursor executes the query
cursor.execute(query)
# Fetch statements bring sequential rows from the table into python tuples
employee_1 = cursor.fetchone()
employees_2_3 = cursor.fetchmany(2)
employees_rest = cursor.fetchall()
print(employee_1)
print(employees_rest)
# Insert a new genre

query2 = 'INSERT INTO genres (Name) values ("Funk");'
cursor.execute(query2)
# Before a change is written to the database, it must be committed
conn.commit()
conn.close()

