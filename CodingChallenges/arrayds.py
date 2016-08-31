#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
print len(arr)
for i in reversed(arr):
	print i,
