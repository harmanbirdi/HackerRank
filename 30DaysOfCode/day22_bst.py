#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-binary-search-trees
# __author__ : Harman Birdi
#


class Node:
    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:
    def __init__(self):
        pass

    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def height(self, root):
        # Write your code here
        if root is None:
            return -1

        left = self.height(root.left)
        right = self.height(root.right)

        return 1 + max(left, right)

# Provided by HackerRank
T = int(raw_input())
myTree = Solution()
root = None

for i in range(T):
    data = int(raw_input())
    root = myTree.insert(root, data)

height = myTree.height(root)
print height
