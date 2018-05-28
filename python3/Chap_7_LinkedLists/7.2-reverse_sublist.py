#!/usr/local/bin/python3
from node import ListNode


# def reverse_sublist(L, s, f):
#     prev = None
#     first = L
#     idx = 1
#     while idx < s:
#         prev, first = first, first.next
#         idx += 1

#     # print(idx, prev.data, first.data)

#     sub_iter = first
#     # sub_iter_next = sub_iter.next
#     while idx < f:
#         temp = sub_iter.next
#         # print(idx, sub_iter.data, sub_iter_next.data, sub_iter_next.next.data)
#         # sub_iter, sub_iter_next, sub_iter_next.next = sub_iter_next, sub_iter_next.next, sub_iter_next
#         sub_iter.next, temp.next, prev.next = temp.next, prev.next, temp
#         idx += 1
#         # print(prev.data, prev.next.data)

#     # print(idx, sub_iter.data, sub_iter_next.data)
#     # first.next = sub_iter_next
#     if prev is None: # i.e. start was first elem
#         print("prev is None")
#         return sub_iter

#     # prev.next = sub_iter
#     # print(sub_iter.next.data)
#     return L

def reverse_sublist(L, s, f):
    head = sublist_head = ListNode('HEAD', L)

    for _ in range(1, s):
        sublist_head = sublist_head.next

    sublist_iter = sublist_head.next
    for _ in range(f - s):
        temp = sublist_iter.next
        sublist_iter.next, temp.next, sublist_head.next = temp.next, sublist_head.next, temp

    return head.next


def reverse_list(L):
    head = ListNode('HEAD', L)
    list_iter = head.next
    while list_iter.next:
        temp = list_iter.next
        list_iter.next, temp.next, head.next = temp.next, head.next, temp
    return head.next


if __name__ == '__main__':
    print('Revers a single sublist!')

    n2  = ListNode(2)
    n7  = ListNode(7, n2)
    n5  = ListNode(5, n7)
    n3  = ListNode(3, n5)
    n11 = ListNode(11, n3)
    L = n11

    print("L -> {}".format(L))
    L = reverse_sublist(L, 2, 4)
    print("L -> {}".format(L))

    n2  = ListNode(2)
    n7  = ListNode(7, n2)
    n5  = ListNode(5, n7)
    n3  = ListNode(3, n5)
    n11 = ListNode(11, n3)
    L = n11

    print("L -> {}".format(L))
    L = reverse_sublist(L, 1, 4)
    print("L -> {}".format(L))

    n11  = ListNode(11)
    n7  = ListNode(7, n11)
    n5  = ListNode(5, n7)
    n3 = ListNode(3, n5)
    n2  = ListNode(2, n3)
    L = n2
    print("reverse list:")
    print("L -> {}".format(L))
    L = reverse_list(L)
    print("L -> {}".format(L))
