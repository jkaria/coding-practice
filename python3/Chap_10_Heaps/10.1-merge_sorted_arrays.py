#!/usr/local/bin/python3
import heapq
import itertools


def merge_sorted_arrays(sorted_arrays):
    counter = itertools.count()
    #res = []
    heap = [] # min heap
    itrs = [ iter(a) for a in sorted_arrays]
    for idx, itr in enumerate(itrs):
        try:
            heapq.heappush(heap, (next(itr), next(counter), idx))
        except StopIteration:
            continue # empty array

    while heap:
        # try:
            next_smallest = heap[0]
            #res.append(next_smallest[0])
            yield next_smallest[0]
            itr_idx = next_smallest[2]
            try:
                heapq.heappushpop(heap, (next(itrs[itr_idx]), next(counter), itr_idx))
            except StopIteration:
                heapq.heappop(heap)
        # except IndexError:
        #     break

    #return res


def merge_sotred_arrays_pythonic(sorted_arrays):
    """heapq.merge(*iterables, key=None, reverse=False)
       NOTE: iterables is a variable positional argument
    """
    return list(heapq.merge(*sorted_arrays))


if __name__ == '__main__':
    print('Merge sorted arrays!')
    a = [3, 5, 7]
    b = [0, 6]
    c = [0, 6, 28]
    s_arrays = [a, b, c]
    print("merge_sorted_arrays({}) -> {}".format(s_arrays, list(merge_sorted_arrays(s_arrays))))
    print("merge_sotred_arrays_pythonic({}) -> {}".format(s_arrays,
                                                          merge_sotred_arrays_pythonic(s_arrays)))
