#!/usr/local/bin/python3


def integer_square_root(k):
    l, r = 0, k

    while l <= r:
        # print(l, r)
        mid = (l + r)//2
        if mid**2 > k:
            r = mid - 1
        else:
            l = mid + 1

    return l-1


if __name__ == '__main__':
    print('Compute Interger square root for k')

    print("integer_square_root({}) -> {}".format(16, integer_square_root(16)))
    print("integer_square_root({}) -> {}".format(300, integer_square_root(300)))
    print("integer_square_root({}) -> {}".format(25, integer_square_root(25)))
    print("integer_square_root({}) -> {}".format(21, integer_square_root(21)))
    print("integer_square_root({}) -> {}".format(0, integer_square_root(0)))
    print("integer_square_root({}) -> {}".format(1, integer_square_root(1)))
    print("integer_square_root({}) -> {}".format(2, integer_square_root(2)))
    print("integer_square_root({}) -> {}".format(3, integer_square_root(3)))
    print("integer_square_root({}) -> {}".format(4, integer_square_root(4)))

