#!/usr/local/bin/python3
import collections

cache = collections.defaultdict(None)


def precomputed_reverse(x):
    res = cache.get(x)
    if not res:
        res = 0
        for _ in range(16):
            res = (res << 1) | (x & 1)
            x >>= 1
        cache[x] = res
    # print('{0} -> {1:016b}'.format(x, x))
    # print('{0} -> {1:016b}'.format(res, res))
    return res


def reverse_bits(x):
    print('{0:064b}'.format(x))
    mask_size = 16
    bit_mask  = 0xFFFF

    res = ( precomputed_reverse(x & bit_mask) << 3 * mask_size |
            precomputed_reverse((x >> mask_size) & bit_mask) << 2 * mask_size |
            precomputed_reverse((x >> 2*mask_size) & bit_mask) << mask_size |
            precomputed_reverse((x >> 3 * mask_size & bit_mask)) )

    print('{0:064b}'.format(res))
    return res


if __name__ == "__main__":
    print("")
    reverse_bits((24<<16*3) | (38<<16*2) | (56<<16*1) | 4)
