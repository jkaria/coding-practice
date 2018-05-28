#!/usr/local/bin/python3
from node import BSTNode
import collections


def is_bst(tree, prev_val=float('-inf')):
    """ Time complexity -> O(n) """
    if not tree:
        return True

    if not is_bst(tree.left):
        return False

    if tree.left != None:
        prev_val = tree.left.data

    # print(prev_val, tree.data, tree.left, tree.right)
    return prev_val <= tree.data and is_bst(tree.right, tree.data)


def is_bst_using_bfs(tree):
    """ Breadth First Search avoids going to lower depth
        if BST property is violated right at the start
    """
    print('is_bst_using_bfs')
    NodeWithLimits = collections.namedtuple('NodeWithLimits', ('node', 'min', 'max'))
    check_bounds = collections.deque()
    check_bounds.append((tree, float('-inf'), float('inf')))

    while len(check_bounds) > 0: # or while check_bounds (it is more pythonic)
        node, low, high = check_bounds.popleft()
        if not low <= node.data <= high:
            return False

        if node.left:
            check_bounds.append((node.left, low, node.data))

        if node.right:
            check_bounds.append((node.right, node.data, high))

    return True


if __name__ == '__main__':
    print('Check if a binary tree satisfies the BST property')

    is_bst = is_bst_using_bfs

    tree1 = BSTNode(13, BSTNode(7, right=BSTNode(9)), BSTNode(19, left=BSTNode(17)))
    print('is_bst(tree1) -> ', is_bst(tree1))

    tree2 = BSTNode(13, BSTNode(11, right=BSTNode(9)), BSTNode(19, left=BSTNode(17)))
    print('is_bst(tree2) -> ', is_bst(tree2))

    tree3 = BSTNode(13, BSTNode(7, right=BSTNode(9)), BSTNode(15, left=BSTNode(17)))
    print('is_bst(tree3) -> ', is_bst(tree3))
