#!/usr/local/bin/python3


def sum_root_to_leaf(root, partial_path_sum=0):
    if not root:
        return 0 #not part of any path

    partail_path_sum = 2 * partail_path_sum + root.data #pre-order traversal

    if not root.left and not root.right: #traversal complete
        return partial_path_sum

    return (sum_root_to_leaf(root.left, partial_path_sum) +
            sum_root_to_leaf(root.right, partial_path_sum))


if __name__ == '__main__':
    print('Find the sum of all the root -> leaf paths in a binary tree')
