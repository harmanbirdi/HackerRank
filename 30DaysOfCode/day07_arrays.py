#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-arrays
# __author__ : Harman Birdi
#

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))

# Solution below
# Using reversed iterator instead of reversing array first
for i in reversed(range(n)):
    print arr[i],

print
