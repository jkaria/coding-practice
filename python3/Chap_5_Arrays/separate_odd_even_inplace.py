#!/usr/local/bin/python3

def separate_odd_even(arr):
    next_even, next_odd = 0, len(arr) - 1
    while next_even < next_odd:
        if arr[next_even] % 2 == 0: # next even candidate is actually even
            next_even += 1
        else:
            # odd_val = arr[next_even]
            # arr[next_even] = arr[next_odd]
            # arr[next_odd] = odd_val
            arr[next_even], arr[next_odd] = arr[next_odd], arr[next_even]
            next_odd -= 1


if __name__ == '__main__':
    print("Separate Odd/Even numbers in array. Even(first)!")

    arr = [x for x in range(1, 11)]
    print("Before: {}".format(arr))
    separate_odd_even(arr)
    print("After: {}".format(arr))
