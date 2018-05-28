#!/usr/local/bin/python3
RED, WHITE, BLUE = range(3)


def dutch_flag_partition(pivot_idx, A):
    """Time complexity:  O(2n) => O(n)
       Space complexity: O(1)
       Classifies in double pass
    """
    pivot = A[pivot_idx]
    lt_idx = 0
    for i in range(len(A)):
        if A[i] < pivot:
            A[lt_idx], A[i] = A[i], A[lt_idx]
            lt_idx += 1
    gt_idx = len(A)-1
    for i in reversed(range(len(A))):
        if A[i] > pivot:
            A[gt_idx], A[i] = A[i], A[gt_idx]
            gt_idx -= 1


def dutch_flag_partition_2(pivot_idx, A):
    """Time complexity:  O(n)
       Space complexity: O(1)
       Classifies in a single pass
    """
    pivot = A[pivot_idx]
    lt_idx = 0
    eq_idx = 0
    gt_idx = len(A)-1
    A[eq_idx], A[pivot_idx] = A[pivot_idx], A[eq_idx]
    eq_idx += 1
    while eq_idx < gt_idx:
        if A[eq_idx] > pivot:
            A[gt_idx], A[eq_idx] = A[eq_idx], A[gt_idx]
            gt_idx -= 1
        elif A[eq_idx] == pivot:
            eq_idx += 1
        else: # A[eq_idx] < pivot
            A[lt_idx], A[eq_idx] = A[eq_idx], A[lt_idx]
            eq_idx += 1
            lt_idx += 1


if __name__ == "__main__":
    print("Dutch Flag Parition problem!")
    print("RED:   %d" % RED)
    print("WHITE: %d" % WHITE)
    print("BLUE:  %d" % BLUE)

    A = [7, 1, 6, 8, 3, 5, 2, 9, 4, 10]
    pivot_idx = 5
    print("Before: {}".format(A))
    dutch_flag_partition(pivot_idx, A)
    print("After:  {}".format(A))

    A = [7, 1, 6, 8, 3, 5, 2, 9, 4, 10]
    pivot_idx = 5
    print("Before: {}".format(A))
    dutch_flag_partition_2(pivot_idx, A)
    print("After:  {}".format(A))

    A = [7, 1, 6, 1, 1, 5, 2, 9, 4, 10, 6, 9, 7, 2, 3]
    pivot_idx = 2
    print("Before: {}".format(A))
    dutch_flag_partition_2(pivot_idx, A)
    print("After:  {}".format(A))
