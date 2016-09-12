#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-recursion
# __author__ : Harman Birdi
#


def factorial(x):
    if x >= 1:
        return x * factorial(x - 1)
    else:
        return 1

n = int(raw_input().strip())
print factorial(n)
