import sqlite3

# Reconnect to the database
conn = sqlite3.connect('article.db')
c = conn.cursor()

# Read data from the table
sql = "SELECT * FROM example"
for row in c.execute(sql):
    print("Software: " + row[0])
    print("Version: " + str(row[1]))
    print("Price: " + str(row[2]))

# Close the connection
conn.close()
