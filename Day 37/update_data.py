import sqlite3

# Reconnect to the database
conn = sqlite3.connect('article.db')
c = conn.cursor()

# Update data in the table
sql = "UPDATE example SET Version = 3.5 WHERE Software = 'Python'"
c.execute(sql)

# Read and print updated data
sql = "SELECT * FROM example"
for row in c.execute(sql):
    print(row)

# Commit the changes and close the connection
conn.commit()
conn.close()
