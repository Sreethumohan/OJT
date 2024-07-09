import sqlite3

# Reconnect to the database
conn = sqlite3.connect('article.db')
c = conn.cursor()

# Insert data into the table
c.execute("INSERT INTO example VALUES ('Python', 3.4, 100)")
c.execute("INSERT INTO example VALUES ('Adobe', 10.2, 1000)")
c.execute("INSERT INTO example VALUES ('Office', 16, 1000)")

# Commit the changes and close the connection
conn.commit()
conn.close()
