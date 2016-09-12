#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-loops
# __author__ : Harman Birdi
#

n = int(raw_input().strip())

for i in range(1, 11):
    print '%d x %d = %d' % (n, i, n * i)
