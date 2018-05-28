#!/usr/local/bin/python3
import bisect


def compute_intersection(A, B):
    """ Time complexity -> O(nlogm)
        efficient if n << m
    """
    def is_present(A, k):
        i = bisect.bisect_left(A, k) # bisect_left returns insertion point to the left
        # NOTE if k is already present in A then A[i] = k
        return (k < len(A) and A[i] == k)

    res = []
    if len(A) < len(B):
        o_arr, i_arr = A, B
    else:
        o_arr, i_arr =  B, A
    for i, x in enumerate(o_arr):
        if (i == 0 or x != o_arr[i-1]) and x in i_arr:
            res.append(x)
    return res


def compute_intersection_2(A, B):
    """ O(m) where m > n
        effiecient if m ~ n
    """
    res = []
    b_idx = 0
    for a in A:
        while b_idx < len(B) and B[b_idx] < a:
            b_idx += 1

        if b_idx == len(B):
            break

        # print(a, b_idx, B[b_idx])
        if B[b_idx] == a:
            if len(res) == 0 or res[-1] != a:
                res.append(a)

    return res


if __name__ == '__main__':
    print('Compute intersection of two sorted arrays!')
    A = [2, 3, 3, 5, 5, 6, 7, 7, 8, 12]
    B = [5, 5, 6, 8, 8, 9, 10, 10]

    print("compute_intersection({}, {}) -> {}".format(A, B, compute_intersection(A, B)))

    print("compute_intersection_2({}, {}) -> {}".format(A, B, compute_intersection_2(A, B)))
