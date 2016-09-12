#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-operators
# __author__ : Harman Birdi
#

import math

mealCost = float(raw_input())
tipPercent = int(raw_input())
taxPercent = int(raw_input())

tip = mealCost * tipPercent / 100
tax = mealCost * taxPercent / 100

totalCost = mealCost + tip + tax
(dollars, cents) = str(totalCost).split('.')
cents = int(cents[0:2])

if cents >= 50:
    print "The total meal cost is %d dollars." % math.ceil(totalCost)
else:
    print "The total meal cost is %d dollars." % math.floor(totalCost)
