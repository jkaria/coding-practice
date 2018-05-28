#!/usr/local/bin/python3
import bintrees
import collections


def find_closest_elem_in_sorted_arrays(sorted_arrays):
    min_distance_so_far = float('inf')

    iters = bintrees.RBTree()
    for idx, s_arr in enumerate(sorted_arrays):
        it = iter(s_arr)
        first_min = next(it, None)
        if first_min is not None:
            iters.insert((first_min, idx), it)

    while True:
        min_val, min_idx = iters.min_key()
        max_val = iters.max_key()[0]
        min_distance_so_far = min(max_val - min_val, min_distance_so_far)

        min_itr = iters.pop_min()[1]
        next_min = next(min_itr, None)

        if next_min is None:
            return [min_val] + [key[0] for key in iters.keys()]

        iters.insert((next_min, min_idx), min_itr)


if __name__ == '__main__':
    print('Find closest elements in sorted arrays')

    a = [5, 10, 15]
    b = [3, 6, 9, 12, 15]
    c = [8, 16, 24]

    print("find_closest_elem_in_sorted_arrays([{}, {}, {}] -> {}".format(a, b, c,
                                                                         find_closest_elem_in_sorted_arrays([a, b, c])))
