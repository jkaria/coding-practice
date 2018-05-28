#!/usr/local/bin/python3
import heapq
import itertools
# from merge_sorted_arrays import merge_sorted_arrays

def sort_k_increasing_decreasing_array(arr):
    sorted_arrays = []
    old_direction = direction = None
    s_idx = 0
    s_arr = []
    for idx, val in enumerate(arr):
        old_direction = direction
        direction = val - arr[idx-1]

        if idx < 2:
            s_arr.append(val)
            continue

        if old_direction * direction < 0:
            if old_direction < 0:
                sorted_arrays.append(sorted(s_arr))
            else:
                sorted_arrays.append(s_arr)
            s_arr = [val]
        else:
            s_arr.append(val)

    if old_direction < 0:
        sorted_arrays.append(sorted(s_arr))
    else:
        sorted_arrays.append(s_arr)

    print(sorted_arrays)
    return list(heapq.merge(*sorted_arrays))


def sort_k_increasing_decreasing_array_pythonic(arr):
    class Monotonic(object):
        def __init__(self):
            self._last = float('-inf')

        def __call__(self, curr):
            res = curr < self._last
            self._last = curr
            return res

    sorted_arrays = [list(group)[::-1 if is_decreasing else 1] for is_decreasing, group in itertools.groupby(arr, Monotonic())]

    print(sorted_arrays)
    return list(heapq.merge(*sorted_arrays))


if __name__ == '__main__':
    print('Sort an increasing-decreasing array!')
    arr = [57, 131, 493, 294, 221, 339, 418, 452, 442, 190]
    print('sort_k_increasing_decreasing_array({}) -> {}'.format(arr,
                                                                sort_k_increasing_decreasing_array(arr)))
    print('sort_k_increasing_decreasing_array_pythonic({}) -> {}'.format(arr,
                                                                sort_k_increasing_decreasing_array_pythonic
                                                                (arr)))
