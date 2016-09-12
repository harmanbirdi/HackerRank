#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-abstract-classes
# __author__ : Harman Birdi
#

from abc import ABCMeta, abstractmethod


class Book:
    __metaclass__ = ABCMeta

    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def display(self): pass


# Write MyBook class
class MyBook(Book):
    def __init__(self, title, author, price):
        self.price = price
        Book.__init__(self, title, author)

    def display(self):
        print "Title: %s\nAuthor: %s\nPrice: %d" % (self.title, self.author, self.price)

# Provided by HackerRank template
title = raw_input()
author = raw_input()
price = int(raw_input())
new_novel = MyBook(title, author, price)
new_novel.display()
