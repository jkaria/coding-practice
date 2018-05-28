#!/usr/local/bin/python3


def merge_two_sorted_arrays(A, B):
    """ Time complexity -> O(m+n)
        Space complexity -> O(1)
    """
    m = len(A) # ideally take m, n values as part of function signature
    n = len(B)
    for _ in range(n):
        A.append(None) # create sufficient space in A

    a_idx, b_idx = m - 1, n - 1
    # print(A)
    # print(list(range(m+n)))
    for idx in reversed(range(m+n)):
        # print(idx, a_idx, A[a_idx], b_idx, B[b_idx])
        if b_idx < 0 or (a_idx >= 0 and A[a_idx] >= B[b_idx]):
            A[idx] = A[a_idx]
            a_idx -= 1
        else:
            A[idx] = B[b_idx]
            b_idx -= 1
        # print(A)



if __name__ == '__main__':
    print('Merge two sorted arrays with result in first array!')

    A = [5, 13, 17]
    B = [3, 7, 11, 19]

    print('merge_two_sorted_arrays({}, {}) -> '.format(A, B))
    merge_two_sorted_arrays(A, B)
    print(A)

