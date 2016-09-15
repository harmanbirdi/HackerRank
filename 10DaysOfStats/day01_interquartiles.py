#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/s10-interquartile-range
# __author__ : Harman Birdi
#


# Gets the median of the list which is the average of the middle
# two numbers of an odd length list, or the middle number of an
# even length list.
def median(l):
    l = sorted(l, key=int)
    mid = len(l) / 2

    if len(l) % 2 == 0:
        return (l[mid - 1] + l[mid]) / 2.0
    else:
        return l[mid] * 1.0


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


# This function creates a new sorted list of its elements and its frequency and
# returns it as a list of integers
def gen_sorted_list(l, f):
    a = map(lambda x, y: (' ' + x) * y, l, f)  # Create list of elements with its frequency
    b = map(lambda x: x.split(), a)  # Split the elements of the list using comma
    c = [item for sublist in b for item in sublist]  # Join sub-lists into a single list
    return map(int, c)


# This function calculates the interquartile range which is the difference between
# quartile3 and quartile1 and returns it.
def interquartile(l, f):
    lf = gen_sorted_list(l, f)  # Create new list from its list and frequencies
    return quartile3(lf) - quartile1(lf)

# Main starts here
n = int(raw_input().strip())
l = raw_input().strip().split()[:n]  # Get n elements from the line as str to use python repeat multiplier
f = map(int, raw_input().strip().split())[:n]  # Get n frequency from the line as integers

print '%.1f' % interquartile(l, f)
