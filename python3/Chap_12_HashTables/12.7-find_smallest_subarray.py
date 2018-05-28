#!/urs/local/bin/python3
import collections


def find_smallest_subarray_with_keys(para, keys):
    result = (None, None)
    # keys_occurence_counter = {} #collections.defaultdict(None) #throws KeyError when None i.e. not found
    keys_occurence_counter = collections.Counter(keys)
    keys_to_find = len(keys)
    left = 0
    for right, word in enumerate(para):
        if word in keys:
            # if word not in keys_occurence_counter or keys_occurence_counter[word] == 0:
            if keys_occurence_counter[word] > 0:
                keys_to_find -= 1
            keys_occurence_counter[word] -= 1
        # print(keys_occurence_counter)

        while keys_to_find == 0:
            if result == (None, None) or right - left < result[1] - result[0]:
                result = (left, right)

            left_word = para[left]
            if left_word in keys:
                keys_occurence_counter[left_word] += 1
                if keys_occurence_counter[left_word] > 0:
                    keys_to_find += 1
            left += 1
            # print(left, right)

    return result


def find_smallest_subarray_with_keys_2(para, keys):
    class DLLNode(object):
        """ Doubly Linked List Node """
        def __init__(self, data=None, prev=None, next=None):
            self.data = data
            self.prev = prev
            self.next = next

    class DLinkedList(object):
        """ Doubly Linked List """
        def __init__(self):
            self.head =  DLLNode('HEAD')
            self.tail = DLLNode('TAIL', self.head)
            self.head.next = self.tail
            self._size = 0

        def __len__(self):
            return self._size

        def append(self, node):
            node.prev = self.tail.prev
            self.tail.prev.next = node
            self.tail.prev = node
            node.next = self.tail
            self._size += 1

        def erase(self, node):
            node.prev.next = node.next
            node.next.prev = node.prev
            self._size -= 1

    def print_dll(dll):
        res = []
        itr = dll.head
        while itr:
            res.append(str(itr.data))
            itr = itr.next
        print('[{}]'.format(', '.join(res)))

    result = (None, None)
    subarray = DLinkedList()
    last_occurence = {}
    for idx, word in enumerate(para):
        if word in keys:
            if word in last_occurence:
                subarray.erase(last_occurence[word])
            node = DLLNode(idx)
            subarray.append(node)
            last_occurence[word] = node

        print_dll(subarray)
        if len(subarray) == len(keys):
            if result == (None, None) or subarray.head.next.data - subarray.tail.prev.data < result[1] - result[0]:
                result = (subarray.head.next.data, subarray.tail.prev.data)

    return result


if __name__ == '__main__':
    print('Find smallest subarray containing set')
    find_smallest_subarray_with_keys = find_smallest_subarray_with_keys_2
    para = ['apple', 'banana', 'apple', 'apple', 'dog', 'cat', 'apple', 'dog', 'banana', 'apple', 'cat', 'dog']
    keys = set(['banana', 'cat'])
    print('find_smallest_subarray_with_keys({}, {}) -> {}', para, keys, find_smallest_subarray_with_keys(para, keys))

    para = ['cat', 'cat', 'cat', 'cat', 'dog']
    keys = set(['cat', 'dog'])
    print('find_smallest_subarray_with_keys({}, {}) -> {}', para, keys, find_smallest_subarray_with_keys(para, keys))

    para = ['dog', 'mouse', 'cat', 'cat', 'cat', 'cat']
    keys = set(['cat'])
    print('find_smallest_subarray_with_keys({}, {}) -> {}', para, keys, find_smallest_subarray_with_keys(para, keys))
