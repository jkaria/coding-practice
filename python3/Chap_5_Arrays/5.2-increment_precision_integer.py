#!/usr/local/bin/python3


# def plus_one(A):
#     A[-1] += 1
#     for i in reversed(range(1, len(A))):
#         # print(i, A)
#         # A[i] += 1
#         if A[i] != 10:
#             # print("Break: ", i, A[i])
#             break
#         A[i] = 0
#         A[i - 1] += 1

#     if A[0] == 10:
#         A[0] = 0
#         A.insert(0, 1)


def plus_one(A):
    idx = len(A) - 1
    # carry = 1
    while idx >= 0:
        A[idx] += 1
        if A[idx] < 10:
            break
        A[idx] = 0
        idx -= 1

    if A[0] == 0:
        A[0] = 0
        A.insert(0, 1)



if __name__ == '__main__':
    print("Problem: Increment An Arbitrary Precision Integer")
    # Test 1
    A = [1, 2, 3]
    print("Before: {}".format(A))
    plus_one(A)
    print("After:  {}".format(A))
    # Test 2
    A = [1, 2, 9]
    print("Before: {}".format(A))
    plus_one(A)
    print("After:  {}".format(A))
    # Test 3
    A = [1, 9, 9]
    print("Before: {}".format(A))
    plus_one(A)
    print("After:  {}".format(A))
    # Test 4
    A = [9, 9, 9]
    print("Before: {}".format(A))
    plus_one(A)
    print("After:  {}".format(A))
    # Test 5
    A = [1, 8, 9]
    print("Before: {}".format(A))
    plus_one(A)
    print("After:  {}".format(A))
