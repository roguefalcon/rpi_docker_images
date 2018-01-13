#!/usr/bin/python3

# Imported libraries
import sqlite3

# The sql connection & cursor
conn = sqlite3.connect('sql.db')
c = conn.cursor()

# List Cars ==================================================================
print("==> Cars")
c.execute('''SELECT rowid,
                    make,
                    model,
                    year,
                    mileage,
                    active
               FROM car''')
data = c.fetchall()

for item in data:
    print(item)

# List Cars ==================================================================
print("==> Passengers")
c.execute('''SELECT rowid,
                    name,
                    active
               FROM passenger''')
data = c.fetchall()

for item in data:
    print(item)

# List Destination ============================================================
print("==> Destinations")
c.execute('''SELECT rowid,
                    street,
                    city,
                    state,
                    zip_code,
                    active
               FROM destination''')
data = c.fetchall()

for item in data:
    print(item)

# List Trip ===================================================================
print("==> Trips")
c.execute('''SELECT rowid,
                    car_id,
                    passenger_id,
                    destination_id,
                    trip_start_time,
                    trip_end_time
               FROM trip''')
data = c.fetchall()

for item in data:
    print(item)
