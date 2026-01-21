import sqlite3

conn = sqlite3.connect('playoffs.db')
cursor = conn.cursor()

query = """
    SELECT *
    FROM teams
"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()

print(records)