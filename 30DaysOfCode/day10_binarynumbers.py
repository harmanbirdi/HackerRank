#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-binary-numbers
# __author__ : Harman Birdi
#

n = int(raw_input().strip())

# Find most consecutive 1's and print max from that list
print max(map(len, str(bin(n))[2:].split('0')))
