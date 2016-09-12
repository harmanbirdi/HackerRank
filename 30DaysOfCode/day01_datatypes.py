#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-data-types
# __author__ : Harman Birdi
#

# Provided by Hacker Rank
i = 4
d = 4.0
s = 'HackerRank'

# My solution below
# Declare second integer, double, and String variables.
j = 0
k = 0.0
l = ""

# Read and save an integer, double, and String to your variables.
j = int(raw_input())
k = float(raw_input())
l = raw_input()

# Print the sum of both integer variables on a new line.
print i + j

# Print the sum of the double variables on a new line.
print d + k

# Concatenate and print the String variables on a new line
# The 's' variable above should be printed first.
print "%s%s" % (s, l)
