#!/usr/local/bin/python3

BASES = '0123456789ABCDEF' # EACH LETTER INDEX IS THE NUMERIC WEIGHT
# NOTE:
# >>> import string
# >>> string.hexdigits
# '0123456789abcdefABCDEF'

def convert_base(num_str, b1, b2):
    # Time complexity -> O(n(1+log(b2,b1)))
    num = 0
    is_neg = False
    if num_str[0] == '-':
        is_neg = True
        num_str = num_str[1:]
    p = 0
    for n in reversed(num_str):
        # print(n, BASES.index(n), b1, p)
        num += BASES.index(n) * b1 ** p
        p += 1

    # print(num)
    res = []
    while num:
        res.append(num % b2)
        num //= b2

    # print(res)

    res_str = '-' if is_neg else ''
    for r in reversed(res):
        res_str += BASES[r]

    return res_str


if __name__ == '__main__':
    print('Base Coversion')

    num_str = '615'
    b1 = 7
    b2 = 13
    res_str = convert_base(num_str, b1, b2)
    print("convert_base({}, {}, {}) -> {}", num_str, b1, b2, res_str)
