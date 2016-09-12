#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-dictionaries-and-maps
# __author__ : Harman Birdi
#

n = int(raw_input())
phonebook = {}  # Dictionary to store key:value pairs as name:number

for i in range(n):
    (name, number) = raw_input().strip().split(' ')
    phonebook[name] = number

while True:
    try:
        name = raw_input().strip()
        try:
            print "%s=%s" % (name, phonebook[name])
        except KeyError:
            print "Not found"
    except EOFError:
        break
