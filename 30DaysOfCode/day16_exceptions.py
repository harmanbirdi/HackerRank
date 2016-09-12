#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-exceptions-string-to-integer
# __author__ : Harman Birdi
#

S = raw_input().strip()

try:
    print int(S)
except:
    print "Bad String"
