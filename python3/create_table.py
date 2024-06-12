import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")


conn.execute('''CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password password NOT NULL
);''')
print("Created table successfully!")

conn.close()