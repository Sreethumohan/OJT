import sqlite3

# Create a connection to the article.db database (or create it if it doesn't exist)
conn = sqlite3.connect('article.db')
c = conn.cursor()

# Create a table named 'example'
c.execute('''
CREATE TABLE IF NOT EXISTS example (
    Software VARCHAR,
    Version REAL,
    Price REAL
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
