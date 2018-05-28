#!/usr/local/bin/python3
from node import ListNode


def merge_sorted_lists(L1, L2):
    """ Assume L1 and L2 are sorted """
    head = tail = ListNode('HEAD')

    while L1 and L2:
        if L1.data <= L2.data:
            tail.next = L1
            L1 = L1.next
        else: # L2.data < L1.data
            tail.next = L2
            L2 = L2.next

        tail = tail.next

    # print(head)
    # print("L1", L1)
    # print("L2", L2)
    tail.next = L1 or L2

    return head.next


def merge_lists(L1, L2):
    res = head = ListNode(data='HEAD')
    tail = ListNode()
    L1, L2 = L1.next, L2.next # filter out dummy head nodes
    while L1 and L2:
        if L1.data <= L2.data:
            head.next = L1
            L1 = L1.next
        else: # L2.data < L1.data
            head.next = L2
            L2 = L2.next
        head = head.next
    while L1:
        head.next = L1
        L1 = L1.next
        head = head.next
    while L2:
        head.next = L2
        L2 = L2.next
        head = head.next

    head = tail

    return res


if __name__ == '__main__':
    print("Merging two sorted linked lists!")
    n7 = ListNode(data=7)
    n5 = ListNode(data=5, next_node=n7)
    n2 = ListNode(data=2, next_node=n5)
    L1 = ListNode(data='HEAD', next_node=n2) # always start with a dummy node

    n11 = ListNode(data=11)
    n3  = ListNode(data=3, next_node=n11)
    L2  = ListNode(data='HEAD', next_node=n3)

    print("L1 -> {}".format(L1))
    print("L2 -> {}".format(L2))
    print("merged -> {}".format(merge_lists(L1, L2)))

    print("-----")
    n7 = ListNode(data=7)
    n5 = ListNode(data=5, next_node=n7)
    n2 = ListNode(data=2, next_node=n5)
    L1 = ListNode(data='HEAD', next_node=n2) # always start with a dummy node

    n11 = ListNode(data=11)
    n3  = ListNode(data=3, next_node=n11)
    L2  = ListNode(data='HEAD', next_node=n3)
    print("L1 -> {}".format(L1))
    print("L2 -> {}".format(L2))
    print("merged -> {}".format(merge_sorted_lists(L1.next, L2.next)))
