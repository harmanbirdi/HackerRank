#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-linked-list
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
    def display(head):
        current = head
        while current:
            print current.data,
            current = current.next

    # Complete this method
    @staticmethod
    def insert(head, data):
        node = Node(data)  # Create new node
        current = head  # Set current to head

        if current is None:  # If empty linked list, return node as head
            return node

        while current.next is not None:  # Otherwise, traverse till end of list where next field is None
            current = current.next
        else:
            current.next = node  # Set the new node to current node's next value

        return head


# Provided by HackerRank template
mylist = Solution()
T = int(input())
head = None

for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)

mylist.display(head)
