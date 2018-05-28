#!/usr/local/bin/python3


def find_majority_element(data):
    if not data:
        return None

    candidate, count = None, 0
    for val in data:
        if count == 0:
            candidate, count = val, 1
        elif val == candidate:
            count += 1
        else: # val != candidate
            count -= 1

    return candidate


if __name__ == '__main__':
    print('Find majority element in stream')
    data = ['b', 'a', 'c', 'a', 'a', 'b', 'a', 'a', 'c', 'a']
    print('find_majority_element:', find_majority_element(data))
    data = ['b', 'a', 'c']
    print('find_majority_element:', find_majority_element(data))
    data = ['b', 'b', 'b', 'a', 'a', 'a', 'a']
    print('find_majority_element:', find_majority_element(data))
    data = ['b', 'b', 'b', 'a', 'a', 'a']
    print('find_majority_element:', find_majority_element(data))

