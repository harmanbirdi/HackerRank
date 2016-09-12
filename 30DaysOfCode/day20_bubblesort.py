#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-sorting
# __author__ : Harman Birdi
#
#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-sorting
# __author__ : Harman Birdi
#


def bubble_sort(ary):
    swap_count = 0

    for i in range(len(ary)):
        swapped = 0
        for j in range(len(ary) - 1):
            if ary[j] > ary[j + 1]:
                ary[j], ary[j + 1] = ary[j + 1], ary[j]
                swapped += 1

        if swapped == 0:
            break

        swap_count += swapped

    return swap_count

# Provided by HackerRank template
n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))

num_swaps = bubble_sort(a)

print "Array is sorted in %d swaps." % num_swaps
print "First Element: %d" % a[0]
print "Last Element: %d" % a[-1]
