#!/bin/python3

import sys


S = input().strip()
try:
	newNumber = int(S)
	print(newNumber)
except:
	print('Bad String')
