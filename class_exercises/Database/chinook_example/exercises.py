import sqlite3

conn = sqlite3.connect('chinook.db')
cursor = conn.cursor()

query = "SELECT FirstName, LastName, Address FROM customers"
cursor.execute(query)
employees_rest = cursor.fetchall()
print(employees_rest)

query3 = "Select City, from playlist_track where "




conn.commit()
conn.close()