#!/usr/local/bin/python3
import heapq


def findRelativeRanks(nums):
    print('')
    """
    :type nums: List[int]
    :rtype: List[str]
    """
    def get_output_value(v):
        res = str(v)
        if v == 1:
            res = 'Gold Medal'
        elif v == 2:
            res = 'Silver Medal'
        elif v == 3:
            res = 'Bronze Medal'
        return res

    max_heap = []
    for i, score in enumerate(nums):
        heapq.heappush(max_heap, (i, -score))

    print(max_heap)
    result = [0]*len(nums)
    rank = 1
    while max_heap:
        idx, val = heapq.heappop(max_heap)
        print(idx, '->', -1*val, rank)
        result[idx] = get_output_value(rank)
        rank += 1

    return result

if __name__ == '__main__':
    print(findRelativeRanks([10,3,8,9,4]))
