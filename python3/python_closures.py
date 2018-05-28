#!/usr/local/bin/python3

class Sorter(object):
    def __init__(self, group):
        self.group = group
        self.found = False

    def __call__(self, num):
        if num in self.group:
            self.found = True
            return (0, num)
        return (1, num)


def sort_priority(numbers, group):
    #print("Values: ", numbers)
    #print("group:  ", group)
    def helper(num):
        if num in group:
            return (0, num)
        return (1, num)

    numbers.sort(key=helper)

    return numbers


if __name__ == '__main__':
    values = [3, 5, 1, 9, 7, 2, 6, 10, 4, 8]
    group = {8, 9, 10}

    result = sort_priority(values, group)

    print("Sorted numbers with preference to group values: ", result, values)

    values1 = [3, 5, 1, 9, 7, 2, 6, 10, 4, 8]
    group = {4, 6, 8}

    sorter = Sorter(group)
    values1.sort(key=sorter)
    print("Using sorter helper. values1: %s, found: %s" % (str(values1), sorter.found))

    values2 = [3, 5, 1, 9, 7, 2, 6, 10, 4, 8]
    group = {11, 12}

    sorter = Sorter(group)
    values2.sort(key=sorter)
    print("Using sorter helper. values2: %s, found: %s" % (str(values2), sorter.found))

