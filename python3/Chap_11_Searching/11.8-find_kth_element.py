#!/usr/local/bin/python3
import copy
import operator
import random


def find_kth_largest(A, k):
    def find_kth(comp):
        def pivot_around_idx(pivot_idx, l, r):
            pivot_val = A[pivot_idx]
            A[r], A[pivot_idx] = A[pivot_idx], A[r]
            new_pivot_idx = l
            for i in range(l, r):
                if comp(A[i], pivot_val):
                    A[i], A[new_pivot_idx] = A[new_pivot_idx], A[i]
                    new_pivot_idx += 1
            A[new_pivot_idx], A[r] = A[r], A[new_pivot_idx]
            return new_pivot_idx

        l, r = 0, len(A) - 1
        while l < r:
            pivot_idx = random.randint(l, r)
            new_pivot_idx = pivot_around_idx(pivot_idx, l, r)
            if new_pivot_idx == k - 1:
                return A[new_pivot_idx]
            elif new_pivot_idx > k - 1:
                right = new_pivot_idx - 1
            else:
                left = new_pivot_idx + 1


    return find_kth(operator.gt)


if __name__ == '__main__':
    print('Find kth largest element')
    A = [3, 7, -1, 8, 51, 2]
    for i in range(len(A)):
        k = i + 1
        print('find_kth_largest({}, {}) -> {}'.format(A, k, find_kth_largest(copy.deepcopy(A), k)))
