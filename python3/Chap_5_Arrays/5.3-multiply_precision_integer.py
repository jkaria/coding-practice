#!/usr/local/bin/python3


def multiply(A, B):
    # TODO: 1. handle negatives
    #       2. trim leading 0's
    """ Time -> O(m*n)
    """
    res = [0] * (len(A) + len(B) + 1)
    for m, b_val in enumerate(reversed(B)):
        print(m, b_val)
        for i, a_val in enumerate(reversed(A)):
            print(i, a_val)
            r_idx = len(res) - (m+i) - 1
            c_idx = r_idx - 1
            mul_res = a_val * b_val + res[r_idx]
            res[r_idx] = mul_res % 10
            res[c_idx] += mul_res // 10
            print(res)
    return res


if __name__ == '__main__':
    print("Problem: Multiply Two Arbitrary Precision Integers")
    # Test 1
    A = [1, 2, 3]
    B = [4, 5, 6]
    print("Multiple({}, {}) -> {}".format(A, B, multiply(A, B)))
    print(123*456)
