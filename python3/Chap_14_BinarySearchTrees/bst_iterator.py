#!/usr/local/bin/python3

# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return "val: {}".format(self.val)

    def __repr__(self):
        return "val: {}".format(self.val)


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self._nodes = []
        if root:
            self._nodes.append(root)


    def hasNext(self):
        """
        :rtype: bool
        """
        print(len(self._nodes))
        return len(self._nodes) > 0


    def next(self):
        """
        :rtype: int
        """
        while self._nodes[-1].left:
            self._nodes.append(self._nodes[-1].left)
        print("next", self._nodes)
        print("size: ", len(self._nodes))
        n = self._nodes.pop()
        print("size: ", len(self._nodes))
        print("next", self._nodes)
        if self._nodes:
            self._nodes[-1].left = None
        if n.right:
            self._nodes.append(n.right)
        print(n.val)
        return n.val


# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
if __name__ == '__main__':
    r = TreeNode(2)
    r.left = TreeNode(1)
    i, v = BSTIterator(r), []
    while i.hasNext(): v.append(i.next())
    print(v)
