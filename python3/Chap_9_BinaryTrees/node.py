#!/usr/local/bin/python3

class BinaryTreeNode(object):

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return "data:{}, left: {}, right: {}".format(self.data, self.left, self.right)
