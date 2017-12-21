#!/usr/bin/python3

# Imported libraries
import sqlite3
import bcrypt

# The sql connection & cursor
conn = sqlite3.connect('sql.db')
c = conn.cursor()

# Make the tables =============================================================
c.execute('''CREATE TABLE IF NOT EXISTS favorite_color
             (name text, color text)''')

c.execute('''CREATE TABLE IF NOT EXISTS users
             (username text, password text)''')

# Let's load some data
c.execute('''INSERT INTO users VALUES (?, ?)''', ('asdf', bcrypt.hashpw(b'asdf', bcrypt.gensalt())))
conn.commit()

