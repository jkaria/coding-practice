#!/usr/local/bin/python3
import string


def int_to_str(num):
    is_neg = False
    if num < 0:
        num, is_neg = -num, True
    # print(num)
    digits = []
    while num:
        digits.append(chr(ord('0') + (num % 10)))
        num //= 10
    # print(digits)
    sign = '-' if is_neg else '+'
    return sign + ''.join(reversed(digits))


def str_to_int(num_str):
    num = 0
    is_neg = False
    for s in num_str:
        if s == '-':
            is_neg = True
        else:
            num = num * 10 + string.digits.index(s)

    if is_neg:
        num *= -1

    return num


if __name__ == '__main__':
    print("Test string_to_int and int_to_string")
    print("str_to_int('{}') -> {:d}".format('123', str_to_int('123')))
    print("int_to_str({}) -> '{:s}'".format(123, int_to_str(123)))
    print("str_to_int('{}') -> {:d}".format('-123', str_to_int('-123')))
    print("int_to_str({}) -> '{:s}'".format(-123, int_to_str(-123)))
