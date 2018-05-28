#!/usr/local/bin/python3
from node import ListNode


def has_cycle(L):
    def cycle_len(stop):
        start, size = stop.next, 1 # min cycle size is 1 where node it pointing to itself
        while start != stop:
            size += 1
            start = start.next
        return size

    slow_itr = fast_itr = L
    cycle_exists = False
    while fast_itr and fast_itr.next:
        slow_itr = slow_itr.next
        if slow_itr is fast_itr:
            cycle_exists = True
            break
        fast_itr = fast_itr.next.next
        if slow_itr is fast_itr:
            cycle_exists = True
            break

    if not cycle_exists:
        return None

    c_len = cycle_len(slow_itr)
    c_start = itr = L
    for _ in range(c_len):
        c_start = c_start.next

    while c_start is not itr:
        itr = itr.next
        c_start = c_start.next

    return c_start


if __name__ == '__main__':
    print('Write a function that detects cycle in a linked list')
