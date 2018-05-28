#!/usr/local/bin/python3


def find_first_of_greater_than_k(A, k):
    idx = -1
    L = 0
    U = len(A) - 1
    while L <= U:
        M = (U + L)//2
        if A[M] <= k:
            idx = M + 1
            L = M + 1 # eliminate all the lower indices
                      # because we are interested in the lowest indice greater than k
            # break
        else:
            idx = M
            U = M - 1

    return idx



def find_first_of_k(A, k):
    idx = -1
    L = 0
    U = len(A) - 1
    while L <= U:
        M = L + (U - L)//2
        if A[M] == k:
            idx = M
            U = M - 1 # eliminate all the higher indices even if they are equal to k
                      # because we are interested in the lowest indice equal to k
            # break
        elif A[M] > k:
            U = M - 1
        else:
            L = M + 1

    # # print(idx)
    # while idx > 1:
    #     if A[idx - 1] != k:
    #         break
    #     idx -= 1

    return idx

if __name__ == '__main__':
    print('Find first occurence of k')
    A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    k = 108
    print('find_first_of_k({}, {}) -> {}'.format(A, k, find_first_of_k(A, k)))
    k = 285
    print('find_first_of_k({}, {}) -> {}'.format(A, k, find_first_of_k(A, k)))

    k = 285
    print('find_first_of_greater_than_k({}, {}) -> {}'.format(A, k, find_first_of_greater_than_k(A, k)))
    k = -13
    print('find_first_of_greater_than_k({}, {}) -> {}'.format(A, k, find_first_of_greater_than_k(A, k)))
    A = [9, 9, 9, 9] #list(range(5))
    # print(len(A))
    k = 5
    print('find_first_of_greater_than_kk.({}, {}) -> {}'.format(A, k, find_first_of_greater_than_k(A, k)))
