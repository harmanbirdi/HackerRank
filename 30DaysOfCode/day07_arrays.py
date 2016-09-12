#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-arrays
# __author__ : Harman Birdi
#

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

# Solution below
arr.reverse()

for i in range(n):
    print arr[i],

print
