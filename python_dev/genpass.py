#!/usr/bin/python3

import crypt

plaintext = 'studentslearncod3#'

hashed = crypt.crypt(plaintext, 'aa')

print(hashed)
