import sqlite3

conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()

query = "SELECT FirstName, LastName, Address FROM customers"
cursor.execute(query)
employees_rest = cursor.fetchall()
print(employees_rest)

query2 = "SELECT * FROM media_types WHERE MediaTypeId = 2"
cursor.execute(query2)
protected = cursor.fetchall()
print(protected)

query3 = "SELECT City FROM customers"
cursor.execute(query3)
cities = cursor.fetchall()
print(cities)

query4 = """INSERT INTO media_types
          VALUES (?)"""
data = ["Windows Media Audio","FLAC audio file"]
cursor.execute(query4,("Windows Media Audio"))
cursor.execute(query4,("FLAC audio file"))
conn.commit()
conn.close()