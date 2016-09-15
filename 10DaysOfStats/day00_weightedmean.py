#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/s10-weighted-mean
# __author__ : Harman Birdi
#


def weighted_mean(x_list, w_list):
    return sum(map(lambda x, y: x * y, x_list, w_list)) / float(sum(w_list))

# Main starts here
n = int(raw_input().strip())
xl = map(int, raw_input().strip().split())[:n]  # Get only first n elements from the line for x list
wl = map(int, raw_input().strip().split())[:n]  # Get only first n elements from the line for weight list

print '%.1f' % weighted_mean(xl, wl)
