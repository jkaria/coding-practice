#!/usr/local/bin/python3

def maximalRectangle(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    def find_ht(r, c):
        count = 0
        while r < len(matrix) and matrix[r][c] == '1':
            count += 1
            r += 1
        return count

    max_area = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == '1':
                w, h = 0, 0
                while c + w < len(matrix[r]) and matrix[r][c + w] == '1':
                    h = min(h, find_ht(r, c + w))
                    w += 1
                    max_area = max(max_area, h * w)

    return max_area

def max_rectangle_in_matrix(matrix):
    if matrix == [] or matrix == [[]]:
        return 0

    heights, max_area = [0] * len(matrix[0]), 0

    for row in matrix:
        for i in range(len(row)):
            heights[i] = heights[i] + 1 if row[i] == '1' else 0
        prev_ht_idxs = []
        for i, ht in enumerate(heights + [0]):
            while prev_ht_idxs and heights[prev_ht_idxs[-1]] >= ht:
                h = heights[prev_ht_idxs.pop()]
                w = i - prev_ht_idxs[-1] - 1 if prev_ht_idxs else i
                max_area = max(h * w, max_area)
            prev_ht_idxs.append(i)

    return max_area


def largest_rectangle(heights):
    prev_ht_idxs, max_area = [], 0

    for i, ht in enumerate(heights + [0]):
        while prev_ht_idxs and heights[prev_ht_idxs[-1]] >= ht:
            h = heights[prev_ht_idxs.pop()]
            w = i - prev_ht_idxs[-1] - 1 if prev_ht_idxs else i
            max_area = max(h * w, max_area)
        prev_ht_idxs.append(i)
    return max_area


def maximalSquare(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    max_size, tracker = 0, []
    for i in range (len(matrix)):
        tracker.append([0] * len(matrix[i]))
        for j in range (len(matrix[i])):
            tracker[i][j] = int(matrix[i][j])
            if i == 0 or j == 0:
                max_size = max(max_size, tracker[i][j])
                continue
            # print('i:', i, ", j:", j, 'matrix[i][j]: ', matrix[i][j])
            if tracker[i][j] == 1:
                print('i:', i, ", j:", j)
                tracker[i][j] = min(tracker[i-1][j], tracker[i][j-1], tracker[i-1][j-1]) + 1
                max_size = max(max_size, tracker[i][j])

    return max_size * max_size


if __name__ == '__main__':
    print('Find max area in rectangle')
    a = [["1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","0"],["1","1","1","1","1","0","0","0"],["0","1","1","1","1","0","0","0"]]

    print("maxRectangle result: expected: 21, actual:", maximalRectangle(a))
    print("max_rectangle_in_matrix result: expected: 21, actual:", max_rectangle_in_matrix (a))

    hts = [2,1,5,6,2,3]
    print("largest_rectangle: ", largest_rectangle(hts))

    matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    for r in matrix:
        print(" ".join(r))
    print("---------------")
    print("maximalSqure:", maximalSquare(matrix))
    # for r in matrix:
    #     print(" ".join(r))
    # print("---------------")
    matrix = [["1"]]
    for r in matrix:
        print(" ".join(r))
    print("---------------")
    print("maximalSqure:", maximalSquare(matrix))
