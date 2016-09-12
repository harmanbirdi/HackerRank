#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-binary-trees
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

    # Write you code here
    bft = []  # Traversal array
    q = []    # Used for levelOrderTraversal

    def levelOrder(self, root):
        # Write your code here
        if root is None:
            return -1

        if root is not None:
            self.q.insert(0, root)
            while len(self.q):
                tree = self.q.pop()
                self.bft.append(tree.data)
                if tree.left is not None:
                    self.q.insert(0, tree.left)
                if tree.right is not None:
                    self.q.insert(0, tree.right)

        print ' '.join(map(str, self.bft))
        return


# Provided by HackerRank template
T = int(raw_input())
myTree = Solution()
root = None

for i in range(T):
    data = int(raw_input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
