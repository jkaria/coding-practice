#!/usr/local/bin/python3


class ReadVisits(object):
    def __init__(self, file):
        self.file = file

    def __iter__(self):
        with open(self.file) as f:
            for line in f:
                yield int(line)


def normalized_defensive_itr(visits_data):
    if iter(visits_data) is iter(visits_data):
        raise TypeError('Must supply a container')
    total = sum(visits_data)
    return (visit*100.0/total for visit in visits_data)


def read_file_data(file):
    with open(file) as f:
        for line in f:
            yield int(line)


def normalized_data(get_file_data_itr):
    total = sum(get_file_data_itr())
    results = []
    for data in get_file_data_itr():
        percent = data*100.0/total
        results.append(percent)
    return results


if __name__ == '__main__':
    visits_file_path = '/Users/jaydeepkaria/projects/python3/visitors_data.txt'
    print("\n------\nAnalyzing city visitors data from file: %s" % visits_file_path)

    result = normalized_data(lambda: read_file_data(visits_file_path))
    print("Normalized data: ", result)
    print("")
    print("Normalized data (2 decimal precision): ")
    print("{:*^9s}, {:*^9s}".format("new", "old"))
    for r in result: # new vs old formatting styles
        #       new                   old
        print("{:>6.2f}".format(r), "%6.2f" % r)
    print("\n")
    print('{:*<30}'.format('left aligned'))
    print('{:*>30}'.format('right aligned'))
    print('{:*^30}'.format('centered'))
    print("\n")
    print('{left:<20} | {center:^20} | {right:>20}'.format(left='left',
                                                           right='right',
                                                           center='center'))

    visits_reader = ReadVisits(visits_file_path)
    itr = normalized_defensive_itr(visits_reader)
    print("\n------\nUsing container:")
    print("Normalized data itr: ", itr)
    print("Normalized data: ", list(itr))

    # Will raise exception
    normalized_defensive_itr(iter([15, 23, 34]))
