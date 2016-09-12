#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-conditional-statements
# __author__ : Harman Birdi
#

N = int(raw_input().strip())

if N % 2 != 0:  # Odd numbers are weird
    print 'Weird'
elif N % 2 == 0:  # Even numbers
    if 2 <= N <= 5:  # Not weird scenario
        print 'Not Weird'
    elif 6 <= N <= 20:  # Weird scenario
        print 'Weird'
    elif 20 < N <= 100:  # Everything else range bound
        print 'Not Weird'
