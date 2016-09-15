#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/s10-quartiles
# __author__ : Harman Birdi
#


# Gets the median of the list which is the average of the middle
# two numbers of an odd length list, or the middle number of an
# even length list.
def median(l):
    l = sorted(l, key=int)
    mid = len(l) / 2

    if len(l) % 2 == 0:
        return (l[mid - 1] + l[mid]) / 2
    else:
        return l[mid]


# Gets quartile1 by calling median with first half of the list
# to get its median, which is the first quartile value.
def quartile1(l):
    l = sorted(l, key=int)
    return median(l[0: len(l) / 2])


# Gets quartile3 by calling median with second half of the list
# to get its median, which is the third quartile value.
def quartile3(l):
    l = sorted(l, key=int)

    if len(l) % 2 == 0:
        return median(l[len(l) / 2:])
    else:
        return median(l[1 + len(l) / 2:])


# Main starts here
n = int(raw_input().strip())
l = map(int, raw_input().strip().split())[:n]  # Get only first n elements from the line

print int(quartile1(l))
print int(median(l))
print int(quartile3(l))
