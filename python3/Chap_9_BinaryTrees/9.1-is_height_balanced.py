#!/usr/local/bin/python3
from collections import namedtuple
from node import BinaryTreeNode

def is_height_balanced(root):
    """ returns tuple (parent's height, subtree/self is_balanced)
        Time: O(n)
        Storage: O(n)
    """
    left_ht_b = (-1, True)
    if root.left:
        # print("left exists for {}".format(root.data))
        left_ht_b = is_height_balanced(root.left)
        #NOTE: if left tree is not balanced not need to check further, directly return False
        if not left_ht_b[1]:
            return (0, False)

    right_ht_b = (-1, True)
    if root.right:
        # print("right exists for {}".format(root.data))
        right_ht_b = is_height_balanced(root.right)

    ht = max(left_ht_b[0], right_ht_b[0]) + 1
    is_balanced = left_ht_b[1] and right_ht_b[1] and (abs(left_ht_b[0] - right_ht_b[0]) <= 1)
    return (ht, is_balanced)


def is_balanced_binary_tree(tree):
    # print("is_balanced_binary_tree")
    BalancedStatusWithHeight = namedtuple('BalancedStatusWithHeight',
                                          ('balanced', 'height'))

    def check_balanced(tree):
        # returns named tuple BalancedStatusWithHeight
        # if balanced then height value represents height of tree
        if not tree:
            return BalancedStatusWithHeight(True, -1)

        left_res = check_balanced(tree.left)
        if not left_res.balanced:
            # Left tree is not balanced, immediately return
            return BalancedStatusWithHeight(False, 0)

        right_res = check_balanced(tree.right)
        if not right_res.balanced:
            # Right tree is not balanced, immediately return
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_res.height - right_res.height) <=1
        height = max(left_res.height, right_res.height) + 1
        return BalancedStatusWithHeight(is_balanced, height)

    return check_balanced(tree).balanced


def largest_complete_binary_tree(tree):
    Tracker = namedtuple('Tracker', ('iscomplete', 'isfull', 'size'))

    def check_completeness(tree):
        if not tree:
            return Tracker(True, True, 0)

        left_status = check_completeness(tree.left)
        right_status = check_completeness(tree.right)
        # print("left: {}, right: {}".format(left_status, right_status))

        size = 0
        iscomplete = False
        isfull = False
        if left_status.iscomplete and right_status.iscomplete:
            iscomplete = left_status.isfull or left_status.size > right_status.size

        if iscomplete: #this tree is complete
            size = left_status.size + right_status.size + 1
            isfull = left_status.size == right_status.size
        else: # persist the largest complete subtree size
            size = max(left_status.size, right_status.size)

        tracker = Tracker(iscomplete, isfull, size)
        print("at {} -> {}".format(tree.data, tracker))

        return tracker

    return check_completeness(tree).size


if __name__ == '__main__':
    print('Test if a binary tree is height balanced!')
    is_height_balanced = is_balanced_binary_tree

    tree = BinaryTreeNode(data='A')
    print("is_height_balanced -> {}".format(is_height_balanced(tree))) #1 , True

    tree.left = BinaryTreeNode(data='B')
    print("is_height_balanced -> {}".format(is_height_balanced(tree))) #2, True

    tree.right = BinaryTreeNode(data='K')
    print("is_height_balanced -> {}".format(is_height_balanced(tree))) #2, True

    tree.left = BinaryTreeNode('B', BinaryTreeNode('C'),
                                    BinaryTreeNode('H'))
    print("is_height_balanced -> {}".format(is_height_balanced(tree))) #3, True

    tree.left.left = BinaryTreeNode('C',
                                    left=BinaryTreeNode('D'))
    print("is_height_balanced -> {}".format(is_height_balanced(tree))) #4, False

    tree.left.right = BinaryTreeNode('H',
                                    BinaryTreeNode('I'))
    print("is_height_balanced -> {}".format(is_height_balanced(tree))) #4, False

    tree.right.right = BinaryTreeNode('O',
                                      BinaryTreeNode('P'))
    print("is_height_balanced -> {}".format(is_height_balanced(tree))) #4, True

    tree.right.left = BinaryTreeNode('L',
                                     BinaryTreeNode('M'),
                                     BinaryTreeNode('N'))
    print("is_height_balanced -> {}".format(is_height_balanced(tree))) #4, True

    print("largest_complete_binary_tree ->", largest_complete_binary_tree(tree))

    print("largest_complete_binary_tree ->", largest_complete_binary_tree(None))
    tree = BinaryTreeNode('A')
    print("largest_complete_binary_tree ->", largest_complete_binary_tree(tree))
    tree.left = BinaryTreeNode('B')
    print("largest_complete_binary_tree ->", largest_complete_binary_tree(tree))
    tree.right = BinaryTreeNode('C')
    print("largest_complete_binary_tree ->", largest_complete_binary_tree(tree))
