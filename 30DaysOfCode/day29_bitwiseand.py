#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-bitwise-and
# __author__ : Harman Birdi
#


# TODO: Couple of testcases are failing - need to fix this.
def find_max(n, k):
    if n == k:
        return 0

    if k in map(lambda x: 2 ** x, range(4, 10)):
        return k - 2

    return k - 1


# Provided by HackerRank template
t = int(raw_input().strip())

for a0 in xrange(t):
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    print find_max(n, k)
