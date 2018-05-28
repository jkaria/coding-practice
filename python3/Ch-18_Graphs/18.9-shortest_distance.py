#!/usr/local/bin/python3
import heapq
import collections

DistanceWithEdgeCount = collections.namedtuple('DistanceWithEdgeCount', ('min_distance', 'min_count'))

Edge = collections.namedtuple('Edge', ('vertex', 'distance'))

class Vertex:
    def __init__(self, id=0):
        self.min_dist_with_edge_count = DistanceWithEdgeCount(float('inf'), 0)
        self.edges = []
        self.id = id
        self.prev = None

    def __lt__(self, other):
        if self.min_dist_with_edge_count != other.self_dist_with_edge_count:
            return self.min_dist_with_edge_count < other.self_dist_with_edge_count
        return self.id < other.id


def dikstras_shortest_path(s, e):
    s.min_dist_with_edge_count = DistanceWithEdgeCount(0, 0)
    min_heap = [s]

    while min_heap:
        smallest = heapq.heappop(min_heap)
        if smallest.id == e.id:
            break

        for e in smallest.edges:
            e_dist = smallest.min_distance_with_edge_count.min_distance + e.distance
            e_edge_count = smallest.min_distance_with_edge_count.min_count + 1

            candidate = DistanceWithEdgeCount(e_dist, e_edge_count)

            if candidate < e.vertex.min_dist_with_edge_count:
                heapq.heappop(min_heap, e.vertex)
                e.vertex.prev = smallest
                e.vertex.min_dist_with_edge_count = candidate
                heapq.heappush(min_heap, e.vertex)

    def print_path(v):
        while v:
            print_path(v.prev)
            print(v.id, ' -> ', end='')

    print_path(e)


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    mapping = collections.defaultdict(list)
    for s in strs:
        mapping[''.join(sorted(s))].append(s)

    return list(mapping.values())

def birthdayCakeCandles(n, ar):
    max_so_far = 0
    count = 0
    for h in ar:
        if h == max_so_far:
            count += 1
        elif h > max_so_far:
            max_so_far = h
            count = 1

    # print(count)
    return count

def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    res = []
    mid = numRows//2
    even = False if numRows % 2 else True
    if even:
        mid -=1
    idx = 0
    filling_mid = False
    subarr = []
    print("is even: ", even, " mid:", mid)
    while idx < len(s):
        if filling_mid:
            if len(subarr) == mid or (even and len(subarr) == mid + 1):
                subarr.append(s[idx])
                idx += 1
            else:
                subarr.append("")
        else:
            subarr.append(s[idx])
            idx += 1

        if len(subarr) == numRows:
            res.append(subarr)
            subarr = []
            filling_mid = not filling_mid

    if len(subarr):
        for _ in range(numRows - len(subarr)):
            subarr.append('')
        res.append(subarr)

    r_str = []
    for i in range(numRows):
        for r in res:
            r_str.append(r[i])

    print(r_str)
    return ''.join(r_str)

if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(strs))

    n = 10
    ar = [int(c) for c in "18 90 90 13 90 75 90 8 90 43".split()]
    print(birthdayCakeCandles(n, ar))

    print(convert("ABC", 2))
