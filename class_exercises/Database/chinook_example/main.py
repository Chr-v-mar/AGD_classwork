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

# Print out employees
print(employee_1)
print(employees_2_3)
print(employees_rest)

# Insert a new genre
cursor = conn.cursor()
query = 'INSERT INTO genres (Name) values ("Funk");'
cursor.execute(query)
# Before a change is written to the database, it must be committed
conn.commit()

# Create a multitable query
query = """SELECT playlists.name, tracks.Name
            FROM playlists JOIN playlist_track pt on playlists.PlaylistId = pt.PlaylistId
            JOIN tracks on pt.TrackId = tracks.TrackId
            WHERE playlists.Name LIKE "Classical%"
            ORDER BY playlists.Name, tracks.Name;"""
cursor.execute(query)
playlist_tracks = cursor.fetchall()


# Close the connection at the end
conn.close()