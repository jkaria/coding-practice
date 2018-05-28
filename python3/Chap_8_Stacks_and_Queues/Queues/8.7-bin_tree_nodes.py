#!/usr/local/bin/python3
from collections import deque


class BinaryTreeNode(object):

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return "data:{}, left: {}, right: {}".format(self.data, self.left, self.right)


def bin_tree_depth_order(root):
    # print(root)
    res = []
    level_nodes = [root]
    while True:
        sub_res = []
        next_nodes = []
        for node in level_nodes:
            sub_res.append(node.data)
            if node.left:
                next_nodes.append(node.left)
            if node.right:
                next_nodes.append(node.right)

        res.append(sub_res)

        if len(next_nodes) == 0:
            break

        level_nodes = next_nodes

    return res


if __name__ == '__main__':
    print('Computing Binary Tree Nodes in increasing depth order using Queue!')
    tree = BinaryTreeNode(314)
    tree.left = BinaryTreeNode(data=6,
                               left=BinaryTreeNode(271,
                                                   left=BinaryTreeNode(28),
                                                   right=BinaryTreeNode(0)),
                               right=BinaryTreeNode(561,
                                                    right=BinaryTreeNode(3,
                                                                         left=BinaryTreeNode(17))))
    tree.right = BinaryTreeNode(data=6,
                                left=BinaryTreeNode(2,
                                                    right=BinaryTreeNode(1,
                                                                         left=BinaryTreeNode(401,
                                                                                             right=BinaryTreeNode(641)),
                                                                         right=BinaryTreeNode(257)
                                                                         )
                                                    ),
                                right=BinaryTreeNode(271,
                                                     right=BinaryTreeNode(28)))

    res = bin_tree_depth_order(tree)
    print(res)
