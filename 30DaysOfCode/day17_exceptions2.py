#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-more-exceptions
# __author__ : Harman Birdi
#


# Write your code here
class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def power(n, p):
        try:
            if n < 0 or p < 0:
                raise ValueError("n and p should be non-negative")
            else:
                return n ** p
        finally:
            pass

# Provided by HackerRank template
myCalculator = Calculator()
T = int(raw_input())
for i in range(T):
    n, p = map(int, raw_input().split())
    try:
        ans = myCalculator.power(n, p)
        print ans
    except Exception, e:
        print e
