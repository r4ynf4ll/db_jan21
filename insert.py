import sqlite3
conn = sqlite3.connect('playoffs.db')
cursor = conn.cursor()

query = """
    INSERT INTO teams(city,name)
    VALUES
    ('Los Angeles','Rams'),
    ('Seattle','Seahawks'),
    ('Denver','Broncos'),
    ('New England','Patriots')
"""

cursor.execute(query)
conn.commit()
conn.close()
