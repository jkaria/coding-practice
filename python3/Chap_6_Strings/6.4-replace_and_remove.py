#!/usr/local/bin/python3
import functools


def replace_and_remove(size, s):
    w_idx = 0
    num_a = 0
    for i in range(size): # erase b's
        if s[i] != 'b':
            s[w_idx] = s[i]
            w_idx += 1
            if s[i] == 'a':
                num_a += 1

    r_idx = w_idx - 1
    w_idx = w_idx + num_a - 1
    # print(size, r_idx, w_idx)
    while r_idx >= 0:
        if s[r_idx] == 'a':
            # s[w_idx] = 'd'
            # w_idx -= 1
            # s[w_idx] = 'd'
            # w_idx -= 1
            s[w_idx - 1 : w_idx + 1] = 'dd'
            w_idx -= 2
        else:
            s[w_idx] = s[r_idx]
            w_idx -= 1

        r_idx -= 1

    return s


if __name__ == '__main__':
    print('Replace a with dd and erase d')

    s = 'acdbbca'
    s_list = list(s)
    print('replace_and_remove({}) -> {}'.format(s, ''.join(replace_and_remove(len(s), s_list ))))
