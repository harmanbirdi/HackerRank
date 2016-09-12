#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-regex-patterns
# __author__ : Harman Birdi
#


def query(fn, email):
    if '@gmail.com' in email:
        return fn

N = int(raw_input().strip())
firstNames = []

for a0 in xrange(N):
    firstName, emailID = raw_input().strip().split(' ')
    firstName, emailID = [str(firstName), str(emailID)]
    firstNames.append(query(firstName, emailID))

firstNames = filter(lambda x: x is not None, sorted(firstNames))
print '\n'.join(sorted(firstNames))
