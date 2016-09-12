#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-2d-arrays
# __author__ : Harman Birdi
#


def hourglass(arry, sr, sc):
    total = 0

    for k in range(sr, sr + 3):
        for l in range(sc, sc + 3):
            # Skip of 2nd row first and third column, to make hourglass
            if (k, l) == (sr + 1, sc) or (k, l) == (sr + 1, sc + 2):
                pass
            else:
                total += arry[k][l]

    return total


# Main starts here
arr = []
for arr_i in xrange(6):
    arr_temp = map(int, raw_input().strip().split(' '))
    arr.append(arr_temp)

hourglasses = []  # list of totals of all hourglass arrays
ws = 3  # window size - square of ws by ws

# Process each hourglass
for i in range(6 - ws + 1):
    for j in range(6 - ws + 1):
        hourglasses.append(hourglass(arr, i, j))

print max(hourglasses)
