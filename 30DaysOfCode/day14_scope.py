#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-scope
# __author__ : Harman Birdi
#


class Difference:
    maximum_difference = 0

    def __init__(self, b):
        self.__elements = b

    # Add your code here
    def compute_difference(self):
        self.maximum_difference = max(self.__elements) - min(self.__elements)

# End of Difference class

# Provided by HackerRank template
_ = raw_input()
a = [int(e) for e in raw_input().split(' ')]

d = Difference(a)
d.compute_difference()

print d.maximum_difference
