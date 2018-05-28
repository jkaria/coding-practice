#!/usr/local/bin/python3
import math
import bintrees

class ABSqrt2:
    def __init__(self, a, b):
        self.a, self.b = a, b
        self.val = a + b * math.sqrt(2)

    def __lt__(self, other):
        return self.val < other.val

    def __eq__(self, other):
        return self.val == other.val

    def __str__(self):
        return "a: {}, b: {}, val: {}".format(self.a, self.b, self.val)


def generate_k_smallest(k):
    """ Time  Complexity: k * O(k)
        Space Complexity: k
    """
    res = []
    candidates = bintrees.RBTree([(ABSqrt2(0, 0), None)])

    while len(res) < k:
        next_min = candidates.pop_min()[0]
        res.append(next_min)
        candidates[ABSqrt2(next_min.a + 1, next_min.b)] = None
        candidates[ABSqrt2(next_min.a, next_min.b + 1)] = None

    return res


if __name__ == '__main__':
    print('Find k smallest A + B * sqrt(2)')

    k = 15
    r = generate_k_smallest(k)
    for i, v in enumerate(r):
        print("{}) {}".format(i + 1, v))
