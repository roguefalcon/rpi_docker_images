#!/usr/bin/python3

# Imported libraries
import sqlite3

# The sql connection & cursor
conn = sqlite3.connect('sql.db')
c = conn.cursor()

# Make the tables =============================================================
c.execute('''SELECT * FROM favorite_color''')
colors = c.fetchall()

for color in colors:
   print(color)

