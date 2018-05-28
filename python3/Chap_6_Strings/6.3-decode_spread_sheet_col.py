#!/usr/local/bin/python3
import functools

def letter_to_idx(l):
    return ord(l) - ord('A') + 1

def decode_ss_col_id(col):
    return functools.reduce(lambda res, l: res * 26 + letter_to_idx(l), col, 0)


if __name__ == '__main__':
    print("Decode spread sheet column to its integer id")

    print('decode_ss_col_id({}) -> {}'.format('D', decode_ss_col_id('D')))
    print('decode_ss_col_id({}) -> {}'.format('A', decode_ss_col_id('AA')))
    print('decode_ss_col_id({}) -> {}'.format('ZZ', decode_ss_col_id('ZZ')))
