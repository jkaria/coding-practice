#!/usr/local/bin/python3
from node import BSTNode


def find_first_node_gt_k_in_bst(tree, k):
    subtree, first_node = tree, None
    while subtree:
        if subtree.data > k:
            subtree, first_node = subtree.left, subtree
        else:
            subtree = subtree.right

    return first_node


if __name__ == '__main__':
    print('Find first value in BST greater than k')

    tree = BSTNode(13, BSTNode(7, right=BSTNode(9)), BSTNode(19, left=BSTNode(17)))
    print('find_first_node_gt_k_in_bst(tree) -> ', find_first_node_gt_k_in_bst(tree, 13))

    tree = BSTNode(13, BSTNode(7, right=BSTNode(9)), BSTNode(19, left=BSTNode(17)))
    print('find_first_node_gt_k_in_bst(tree) -> ', find_first_node_gt_k_in_bst(tree, 19))

    tree = BSTNode(13, BSTNode(7, right=BSTNode(9)), BSTNode(19, left=BSTNode(17)))
    print('find_first_node_gt_k_in_bst(tree) -> ', find_first_node_gt_k_in_bst(tree, 5))
