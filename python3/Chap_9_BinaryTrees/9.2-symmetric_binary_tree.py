#!/usr/local/bin/python3
from node import BinaryTreeNode


def is_symmetric(tree):
    def check_symmetric(subtree_0, subtree_1):
        if not subtree_0 and not subtree_1:
            return True
        elif subtree_0 and subtree_1:
            return (subtree_0.data == subtree_1.data
                    and check_symmetric(subtree_0.left, subtree_1.right)
                    and check_symmetric(subtree_0.right, subtree_1.left))

        # else one is null i.e. not symmetric
        return False

    return not tree or check_symmetric(tree.left, tree.right)


if __name__ == '__main__':
    print('Test if a binary tree is symmetric')

    print("is_symmetric(None) ->", is_symmetric(None))

    single_node = BinaryTreeNode(314)
    print("is_symmetric(single_node) ->", is_symmetric(single_node))

    symtree_1 = BinaryTreeNode(314, BinaryTreeNode(6), BinaryTreeNode(6))
    symtree_1.left.right = BinaryTreeNode(2, right=BinaryTreeNode(3))
    symtree_1.right.left = BinaryTreeNode(2, left=BinaryTreeNode(3))
    print("is_symmetric(symtree_1) ->", is_symmetric(symtree_1))

    symtree_2 = BinaryTreeNode(314, BinaryTreeNode(6), BinaryTreeNode(6))
    symtree_2.left.right = BinaryTreeNode(561, right=BinaryTreeNode(3))
    symtree_2.right.left = BinaryTreeNode(2, left=BinaryTreeNode(3))
    print("is_symmetric(symtree_2) ->", is_symmetric(symtree_2))

    symtree_3 = BinaryTreeNode(314, BinaryTreeNode(6), BinaryTreeNode(6))
    symtree_3.left.right = BinaryTreeNode(561, right=BinaryTreeNode(3))
    symtree_3.right.left = BinaryTreeNode(561)
    print("is_symmetric(symtree_3) ->", is_symmetric(symtree_3))
