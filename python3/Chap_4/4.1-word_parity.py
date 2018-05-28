#!/usr/local/bin/python3

def calculate_parity(number):
    """Returns 1 if # of 1's in binary representation is ODD and 0 if EVEN
       Complexity is O(N) -> N is number of bit
    """
    parity = 0
    while number:
        # print("number -> {}, bin -> {}, parity -> {}".format(number, bin(number), parity))
        parity ^= number & 1
        number >>= 1

    # print("number -> {}, bin -> {}, parity -> {}".format(number, bin(number), parity))
    return parity

def parity(x):
    """saves space as calculates result in place
       complexity is O(log(n)) where n i word size
    """
    x &= 0xFFFF
    x ^= x >> 16 # has result in last 16 bits
    x ^= x >> 8 # has result in last 8 bits
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1 # extracts and returns the result from the last bit


def parity_2(x):
    """complexity is O(k), where k is number of 1's in digit
    """
    result = 0
    while x:
        result ^= 1 # result = (result + 1) % 2
        x &= x - 1
    return result


if __name__ == '__main__':
    print("Find word parity!")

    print("number -> {}, bin -> {}, parity -> {}".format(0, bin(0), calculate_parity(0)))
    print("number -> {}, bin -> {}, parity -> {}".format(1, bin(1), calculate_parity(1)))
    print("number -> {}, bin -> {}, parity -> {}".format(13, bin(13), calculate_parity(13)))
    print("number -> {}, bin -> {}, parity -> {}".format(45, bin(45), calculate_parity(45)))
    print("number -> {}, bin -> {}, parity -> {}".format(125, bin(125), calculate_parity(125)))
    print("")
    print("number -> {}, bin -> {}, parity -> {}".format(0, bin(0), parity(0)))
    print("number -> {}, bin -> {}, parity -> {}".format(1, bin(1), parity(1)))
    print("number -> {}, bin -> {}, parity -> {}".format(13, bin(13), parity(13)))
    print("number -> {}, bin -> {}, parity -> {}".format(45, bin(45), parity(45)))
    print("number -> {}, bin -> {}, parity -> {}".format(125, bin(125), parity(125)))
    print("")
    print("number -> {}, bin -> {}, parity -> {}".format(0, bin(0), parity_2(0)))
    print("number -> {}, bin -> {}, parity -> {}".format(1, bin(1), parity_2(1)))
    print("number -> {}, bin -> {}, parity -> {}".format(13, bin(13), parity_2(13)))
    print("number -> {}, bin -> {}, parity -> {}".format(45, bin(45), parity_2(45)))
    print("number -> {}, bin -> {}, parity -> {}".format(125, bin(125), parity_2(125)))
    print("")
