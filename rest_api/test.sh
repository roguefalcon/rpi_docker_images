#!/bin/bash


# Run the load_sql.py to put us in a stable state
./load_sql.py

echo "==> Testing Passengers"
curl http://192.168.1.112:5001/api/1.0/passenger
curl -X POST -d 'name=Hugo Weaving' http://192.168.1.112:5001/api/1.0/passenger
curl http://192.168.1.112:5001/api/1.0/passenger/4
curl -X PUT -d 'name=Agent Smith' http://192.168.1.112:5001/api/1.0/passenger/4
curl http://192.168.1.112:5001/api/1.0/passenger/4
curl -X DELETE http://192.168.1.112:5001/api/1.0/passenger/4
curl http://192.168.1.112:5001/api/1.0/passenger

echo "==> Testing Cars"
curl http://192.168.1.112:5001/api/1.0/car
curl -X POST -d make=Uber -d model=Volvo -d year=2018 -d mileage=1234 http://192.168.1.112:5001/api/1.0/car
curl http://192.168.1.112:5001/api/1.0/car/4
curl -X PUT -d make=Uber -d model=Racer -d year=2018 -d mileage=1234 http://192.168.1.112:5001/api/1.0/car/4
curl http://192.168.1.112:5001/api/1.0/car/4
curl -X DELETE http://192.168.1.112:5001/api/1.0/car/4
curl http://192.168.1.112:5001/api/1.0/car

echo "==> Testing Destinations"
curl http://192.168.1.112:5001/api/1.0/destination
curl -X POST -d 'street=1234 Main Street' -d city=Hollywood -d state=CA -d zip_code=90028 http://192.168.1.112:5001/api/1.0/destination
curl http://192.168.1.112:5001/api/1.0/destination/4
curl -X PUT -d 'street=1234 Main Street' -d city=Hollywood -d state=CA -d zip_code=90028 http://192.168.1.112:5001/api/1.0/destination/4
curl http://192.168.1.112:5001/api/1.0/destination/4
curl -X DELETE http://192.168.1.112:5001/api/1.0/destination/4
curl http://192.168.1.112:5001/api/1.0/destination

echo "==> Testing Trips"
curl http://192.168.1.112:5001/api/1.0/trip
curl -X POST -d car_id=3 -d passenger_id=1 -d destination_id=2 -d 'trip_start_time=2018-01-18 11:14:07' -d 'trip_end_time=2018-01-18 11:28:19' http://192.168.1.112:5001/api/1.0/trip
curl http://192.168.1.112:5001/api/1.0/trip/4
curl -X PUT -d car_id=2 -d passenger_id=1 -d destination_id=2 -d 'trip_start_time=2018-01-18 11:14:07' -d 'trip_end_time=2018-01-18 11:28:19' http://192.168.1.112:5001/api/1.0/trip/4
curl http://192.168.1.112:5001/api/1.0/trip/4
curl -X DELETE http://192.168.1.112:5001/api/1.0/trip/4
curl http://192.168.1.112:5001/api/1.0/trip
