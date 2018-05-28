#!/usr/local/bin/python3

def delete_duplicates(A):
    if not A:
        return 0

    nex_valid_elem_idx = 1
    for i in range(1, len(A)):
        if A[i] != A[nex_valid_elem_idx - 1]:
            A[nex_valid_elem_idx] = A[i]
            nex_valid_elem_idx += 1

    return nex_valid_elem_idx


if __name__ == '__main__':
    print("Delete duplicates from a sorted array.")

    A = [2, 3, 5, 5, 7, 11, 11, 11, 13]
    print("delete_duplicates from ->", A)
    print('result                 -> {}, valid elems: {}'.format(A, delete_duplicates(A)))

