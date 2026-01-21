import sqlite3
import pandas as pd

conn = sqlite3.connect('playoffs.db')
cursor = conn.cursor()

query = """
    SELECT *
    FROM teams
"""

cursor.execute(query)
records = cursor.fetchall()
conn.close()

records_df = pd.DataFrame(records,columns=['id','city','name'])
print(records_df['city'])

# WAYS TO MANIPULATE DATA
# make list of cities and print them
citynames = []
for record in records:
    citynames.append(record[1])
print(citynames)

# make list of tuples of how many characters are in each city and team name
citylen = []
for record in records:
    chars = (len(record[1]),len(record[2]))
    citylen.append(chars)
print(citylen)