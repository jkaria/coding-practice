#!/usr/local/bin/python3


def search_entry_equal_to_idx(A):
    """ Searches an entry in a sorted array equal to it's index in array """
    start, end = 0, len(A) - 1
    while start <= end:
        mid = (start + end) // 2
        if A[mid] == mid:
            return mid
        elif A[mid] < mid:
            start = mid + 1
        else:
            end = mid - 1
    return -1


if __name__ == '__main__':
    print("Search an entry equal to it's index in a list")
    A = [-4, -3, -2, -1, 0, 2, 3, 6, 7, 9]
    print("search_entry_equal_to_idx({}) -> {}".format(A, search_entry_equal_to_idx(A)))
