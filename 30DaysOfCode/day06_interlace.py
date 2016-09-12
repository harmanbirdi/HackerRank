#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-review-loop
# __author__ : Harman Birdi
#

# Enter your code here. Read input from STDIN. Print output to STDOUT
l = int(raw_input())  # Number of input lines

for i in range(l):
    s = raw_input()
    a = b = ''
    for j in range(len(s)):
        if j % 2 == 0:
            a += s[j]
        else:
            b += s[j]

    print a, b
