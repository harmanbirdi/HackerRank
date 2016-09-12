#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-running-time-and-complexity
# __author__ : Harman Birdi
#

import math


def is_prime(num):
    if num == 1:
        return "Not prime"

    for j in range(2, int(math.ceil(math.sqrt(num)))):
        if num % j == 0:
            return "Not prime"

    return "Prime"


n = int(raw_input())

for i in range(n):
    print is_prime(int(raw_input()))
