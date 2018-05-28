#!/usr/local/bin/python3


def find_ample_city(gallons, distances):
    """ gallons: """
    MPG = 20
    CityAndRemainingGas = collections.namedtuple('CityAndRemainingGas', ('city', 'gas_left'))
    tracker = CityAndRemainingGas(0, 0)
    gas_left = 0
    for i in range(1, len(gallons)):
        gas_left += gallons[i - 1] - distances[i - 1] // MPG
        if gas_left < tracker.gas_left:
            tracker = CityAndRemainingGas(i, gas_left)

    return tracker.city

if __name__ == '__main__':
    print('Gasup problem -> Find the ample city')
