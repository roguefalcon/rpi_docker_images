#!/usr/bin/python3

# Imported libraries
import sqlite3
import bcrypt
import os

# We want to remove the existing file
try:
        os.remove('sql.db')
except OSError as e:
        print("Couldn't remove the file:", e.strerror)

        # The sql connection & cursor
        conn = sqlite3.connect('sql.db')
        c = conn.cursor()

        # Make the tables =============================================================
        c.execute('''CREATE TABLE IF NOT EXISTS session
                     (user_id integer, date_created text)''')

        c.execute('''CREATE TABLE IF NOT EXISTS user
                     (email text, password text, employee_id integer, customer_id integer, status_id integer, active integer, date_created text)''')
        c.execute('''INSERT INTO user VALUES (?, ?, ?, ?, ?, ?, ?)''',
                ('jane.doe@gmail.com', bcrypt.hashpw(b'asdf', bcrypt.gensalt()), '1', '1', '1', '1', '2018-01-27'))

        conn.commit()
