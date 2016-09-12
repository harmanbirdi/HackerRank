#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-testing
# __author__ : Harman Birdi
#


def class_canceled(strength, threshold, attendance):
    late = len(filter(lambda x: x > 0, attendance))
    ontime = len(attendance) - late

    if ontime >= threshold:
        return 'NO'

    return 'YES'

# Main starts here
print '5'
print '5 3'
print '-1 90 999 100 0'
print '4 2'
print '0 -1 2 1'
print '3 3'
print '-1 0 1'
print '6 1'
print '-1 0 1 -1 2 3'
print '7 3'
print '-1 0 1 2 3 4 5'

T = int(raw_input())

for i in range(T):
    (strength, threshold) = map(int, raw_input().split(' '))
    attendance = list(map(int, raw_input().split(' ')))
    print class_canceled(strength, threshold, attendance)
