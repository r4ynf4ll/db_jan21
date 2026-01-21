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

# other way to do this
citynames = []
for record in records:
    citynames.append(record[1])
print(citynames)