#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/s10-basic-statistics
# __author__ : Harman Birdi
#

from collections import Counter
from operator import itemgetter


# This function calculates the average of the numbers in the list
def mean(l):
    return float(reduce(lambda x, y: x + y, l)) / len(l)


# Gets the median of the list which is the average of the middle
# two numbers of an odd length list, or the middle number of an
# even length list.
def median(l):
    l = sorted(l, key=int)
    mid = len(l) / 2

    if len(l) % 2 == 0:
        return (l[mid - 1] + l[mid]) / 2.0
    else:
        return l[mid]


# Returns the most occurring element or the smallest number if the frequency of
# each number occurs the same number of times
def mode(lst):
    lst = sorted(lst, key=int)
    dct = Counter(lst)  # Use counter to create a dictionary of occurence count
    sorted_h = sorted(dct.items(), key=itemgetter(1), reverse=True)  # Descending list of tuples sorted by value

    # In case, items occur more than once, find the max occurence and build a subset of just those
    # and return the element with minimum value of that subset
    if sorted_h[0][1] > 1:
        max_occurence = sorted_h[0][1]
        sublst = []

        for item in sorted_h:
            if item[1] == max_occurence:
                sublst.append(item[0])
            else:
                break

        return min(sublst)

    return lst[0]


# Main starts here
n = int(raw_input().strip())
l = map(int, raw_input().strip().split())[:n]  # Get only first n elements from the line

print '%.1f' % mean(l)
print '%.1f' % median(l)
print mode(l)
