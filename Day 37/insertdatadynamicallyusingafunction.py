import sqlite3

def dynamic_data():
    # Reconnect to the database
    conn = sqlite3.connect('article.db')
    c = conn.cursor()
    
    # Get user input
    soft = input("Write Software Name: ")
    version = input("Write Version: ")
    price = input("Write Price: ")
    
    # Insert data into the table
    c.execute("INSERT INTO example (Software, Version, Price) VALUES (?, ?, ?)", (soft, version, price))
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Call the function to insert data dynamically
dynamic_data()
