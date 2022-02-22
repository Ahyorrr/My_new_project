import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
# the 'INTEGER PRIMARY KEY' enables SQL to automatically add new ids to rows
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name text, price real)"  # real is basically a float
cursor.execute(create_table)


connection.commit()

connection.close()
