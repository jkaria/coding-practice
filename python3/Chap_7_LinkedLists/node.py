#!/usr/local/bin/python3

class ListNode(object):
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

    # # @classmethod
    # def __iter__(self):
    #     if self.next is None:
    #         return
    #     yield self.next

    def __str__(self):
        return "{}, {}".format(self.data, self.next)

def linked_list_to_str(L):
    res = ''
    while L:
        res += L.data
        L = L.next
    return res
