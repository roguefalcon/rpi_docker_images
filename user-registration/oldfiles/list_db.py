#!/usr/bin/python

from tinydb import TinyDB, Query, where

db = TinyDB('db.json')   # The database we are storing this in

# Show the ones we added
print db.all()
