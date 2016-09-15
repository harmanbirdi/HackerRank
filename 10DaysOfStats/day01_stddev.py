#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/s10-standard-deviation
# Additional Info: Using statistics package would defeat the purpose, so going longer route
# __author__ : Harman Birdi
#

import math


# This function calculates the average of the numbers in the list
def mean(l):
    return float(reduce(lambda x, y: x + y, l)) / len(l)


# This function calculates the sum of mean squared distance of each element
# in the list from the mean, and returns it
def sigma_mean_squared_distance(l):
    mu_list = []
    mu = mean(l)

    for i in range(len(l)):
        mu_list.append(mu)

    return reduce(lambda x, y: x + y, map(lambda x, y: (x - y) ** 2, l, mu_list))


# This function calculates the standard deviation, by calculating
# the square root of the sum of mean squared distance of each element
# in the list divided by the total number of elements in the list
def stdev(l):
    return math.sqrt(sigma_mean_squared_distance(l) / len(l))


# Main starts here
n = int(raw_input().strip())
l = map(int, raw_input().strip().split())[:n]  # Get first n elements from the line

print "%.1f" % stdev(l)
