#!/usr/local/bin/python3


def has_three_sum_uniq(A, t):
    def has_two_sum_uniq(idx, sum):
        lb, ub = idx, len(A) - 1
        while True:
            while lb < ub and A[lb] == A[lb + 1]:
                lb += 1
            while ub > lb and A[ub] == A[ub - 1]:
                ub -= 1
            if lb >= ub:
                break
            if A[lb] + A[ub] == sum:
                print(lb, '->', A[lb], ub, '->', A[ub])
                return True
            elif A[lb] + A[ub] < sum:
                lb += 1
            else: # A[lb] + A[ub] > sum
                ub -= 1
        return False

    A.sort()
    i = 0
    while True:
        while i < len(A) - 2 and A[i] == A[i + 1]:
            i += 1
        if i >= len(A) - 2:
            break

        if has_two_sum_uniq(i + 1, t - A[i]):
            print(i, '->', A[i])
            return True

        i += 1

    return False


if __name__ == '__main__':
    print('Find if array has 3 uniq values adding up to target')
    A = [5, 2, 3, 4, 3]
    t = 9
    print('has_three_sum_uniq -> ', has_three_sum_uniq(A, t))
