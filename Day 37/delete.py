import sqlite3

# Reconnect to the database
conn = sqlite3.connect('article.db')
c = conn.cursor()

# Delete data from the table
sql = "DELETE FROM example WHERE Software = 'Python'"
c.execute(sql)

# Read and print remaining data
sql = "SELECT * FROM example"
for row in c.execute(sql):
    print(row)

# Commit the changes and close the connection
conn.commit()
conn.close()
