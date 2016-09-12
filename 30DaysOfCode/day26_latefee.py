#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-nested-logic
# __author__ : Harman Birdi
#


def late_fee(da, ma, ya, de, me, ye):
    fine = 0

    if ya <= ye and ma <= me and da <= de:
        return fine
    elif ya == ye and ma == me and da > de:
        return 15 * (da - de)
    elif ya == ye and ma > me:
        return 500 * (ma - me)
    elif ya > ye:
        return 10000

    return fine

(da, ma, ya) = map(int, raw_input().split(' '))
(de, me, ye) = map(int, raw_input().split(' '))

print late_fee(da, ma, ya, de, me, ye)
