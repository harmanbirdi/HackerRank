#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-linked-list-deletion
# __author__ : Harman Birdi
#


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def __init__(self):
        pass

    @staticmethod
    def insert(head, data):
        p = Node(data)
        if head is None:
            head = p
        elif head.next is None:
            head.next = p
        else:
            start = head
            while start.next is not None:
                start = start.next
            start.next = p

        return head

    @staticmethod
    def display(head):
        current = head
        while current:
            print current.data,
            current = current.next

    # Write your code here
    @staticmethod
    def remove_duplicates(head):
        current = head

        if head is None:
            return head

        while current.next is not None:
            next = current.next
            if current.data == next.data:
                current.next = next.next
                del next
            else:
                current = current.next
        return head

# Provided by HackerRank template
mylist = Solution()
T = int(input())
head = None
for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)

head = mylist.remove_duplicates(head)
mylist.display(head)
