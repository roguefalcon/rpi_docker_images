#!/usr/bin/python3

import crypt
import sys

plaintext = sys.argv[1]
hashed = crypt.crypt(plaintext, 'aa')

print(hashed)
