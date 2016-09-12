#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-class-vs-instance
# __author__ : Harman Birdi
#


class Person:
    age = 0

    def __init__(self, initial_age):
        # Add some more code to run some checks on initial_age
        if initial_age < 0:
            print 'Age is not valid, setting age to 0.'
        else:
            self.age = initial_age

    def am_i_old(self):
        # Do some computations in here and print out the correct statement to the console
        if self.age < 13:
            print 'You are young.'
        elif 13 <= self.age < 18:
            print 'You are a teenager.'
        else:
            print 'You are old.'

    def year_passes(self):
        # Increment the age of the person in here
        self.age += 1

# Provided by Hacker Rank
t = int(raw_input())

for i in range(0, t):
    age = int(raw_input())
    p = Person(age)
    p.am_i_old()
    for j in range(0, 3):
        p.year_passes()
    p.am_i_old()
    print("")
