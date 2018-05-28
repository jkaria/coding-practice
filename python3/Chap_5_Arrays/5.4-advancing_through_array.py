#!/usr/local/bin/python3


def can_reach_end(A):
    furthest_so_far, last_idx = 0, len(A) - 1
    i = 0
    min_steps = 0
    while i <= furthest_so_far and furthest_so_far < last_idx:
        old_farthest = furthest_so_far
        furthest_so_far = max(furthest_so_far, i + A[i])
        if furthest_so_far != old_farthest:
            print('old_so_far: {}, so_far: {}, i: {}, A[i]: {}'.format(old_farthest,
                                                                       furthest_so_far,
                                                                       i, A[i]))
            min_steps += 1
        i += 1

    return furthest_so_far >= last_idx, min_steps


if __name__ == '__main__':
    print("Advancing through an array.")

    A = [2, 4, 1, 1, 0, 2, 3]
    print('can_reach_end({}) -> {}'.format(A, can_reach_end(A)))

    A = [3, 2, 0, 0, 2, 0, 1]
    print('can_reach_end({}) -> {}'.format(A, can_reach_end(A)))
