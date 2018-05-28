#!/usr/local/bin/python3
import collections

W, B = 'W', 'B'

def print_2d(A):
    print('----')
    for a in A:
        print("  ".join(a))
    print('----')


def find_max_blacks(A):
    Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))
    def mark_region(x, y):
        count = 1
        color = A[x][y]
        q = collections.deque([(x, y)])
        A[x][y] = 'V'
        while q:
            i, j = q.popleft()
            for d in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                n_i, n_j = i + d[0], j + d[1]
                # print(n_i, n_j)
                if 0 <= n_i < len(A) and 0 <= n_j < len(A[n_i]) and A[n_i][n_j] == color:
                    count += 1
                    A[n_i][n_j] = 'V'
                    q.append((n_i, n_j))
        print_2d(A)
        print('count: ', count)
        return count

    max_blacks = 0
    for i in range(len(A)):
        for j in range(len(A[i])):
            if A[i][j] == B:
                max_blacks = max(max_blacks, mark_region(i, j))

    return max_blacks




if __name__ == '__main__':
    print('Compute black region with most points in a 2D Array')

    A = [
            [B, B, B, B, B],
            [W, W, B, B, B],
            [B, W, W, W, W],
            [W, W, B, B, B],
            [B, B, B, W, W]
        ]

    print_2d(A)

    print('max_black_region: ', find_max_blacks(A))
