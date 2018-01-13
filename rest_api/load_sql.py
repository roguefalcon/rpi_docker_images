#!/usr/bin/python3

# Imported libraries
import sqlite3
import os

# We want to remove the existing file
try:
    os.remove('sql.db')
except OSError as e:
    print("Couldn't remove the file:", e.strerror)

# The sql connection & cursor
conn = sqlite3.connect('sql.db')
c = conn.cursor()

print("Processing tables")

# Make the cars =============================================================
print("==> Cars")
c.execute('''CREATE TABLE IF NOT EXISTS car
             (   make TEXT,
                model TEXT,
                 year INTEGER,
              mileage INTEGER,
               active INTEGER)''')

# Let's load some data
c.execute('''INSERT INTO car VALUES (?, ?, ?, ?, ?)''',
          ('Tesla', 'Model 27', 2021, 13784, 1))
c.execute('''INSERT INTO car VALUES (?, ?, ?, ?, ?)''',
          ('Google', 'PixelCar Beta', 2018, 35741, 1))
c.execute('''INSERT INTO car VALUES (?, ?, ?, ?, ?)''',
          ('Apple', 'Model XX', 2019, 1337, 1))

# Make the passengers ============================================================
print("==> Passengers")
c.execute('''CREATE TABLE IF NOT EXISTS passenger
             (   name TEXT,
               active INTEGER)''')

# This uses executemany() which is faster for larger sets of data
passengers = [('Keanu Reeves', 1),
              ('Laurence Fishburne', 1),
              ('Carrie-Anne Moss', 1)]
c.executemany('INSERT INTO passenger VALUES (?, ?)', passengers)

# Make the Destinations =======================================================
print("==> Destinations")
c.execute('''CREATE TABLE IF NOT EXISTS destination
             (street TEXT,
                city TEXT,
               state TEXT,
            zip_code INTEGER,
              active INTEGER)''')

# This uses executemany() which is faster for larger sets of data
destinations= [('6801 Hollywood Blvd', 'Los Angeles', 'CA', 90028, 1),
               ('3400 Warner Blvd', 'Burbank', 'CA', 91522, 1),
               ('6801 Hollywood Blvd', 'Hollywood', 'CA', 90028, 1)]
c.executemany('INSERT INTO destination VALUES (?, ?, ?, ?, ?)', destinations)


# Make the Trips =============================================================
print("==> Trips")
c.execute('''CREATE TABLE IF NOT EXISTS trip
              (        car_id INTEGER,
                 passenger_id INTEGER,
               destination_id INTEGER,
              trip_start_time TEXT,
                trip_end_time TEXT)''')

# This uses executemany() which is faster for larger sets of data
destinations= [(1, 1, 1, '2018-01-14 07:14:12', '2018-01-14 07:23:01'),
               (2, 3, 2, '2018-01-14 13:47:39', '2018-01-14 14:01:17'),
               (3, 2, 3, '2018-01-14 06:01:53', '2018-01-14 07:41:19')]
c.executemany('INSERT INTO trip VALUES (?, ?, ?, ?, ?)', destinations)

# Now we need to save the changes to the file
conn.commit()
