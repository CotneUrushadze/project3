import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")

conn.execute('''CREATE TABLE users
            ( user_id int(5) PRIMARY KEY,
            username varchar(25) NOT NULL,
            password varchar(30) NOT NULL
            );''')
print("Created table successfully!")

conn.close()