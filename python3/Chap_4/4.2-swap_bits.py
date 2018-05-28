#!/usr/local/bin/python3


# Arguments are passed by assignment. The rationale behind this is twofold:

#      1. the parameter passed in is actually a reference to an object (but the reference is passed by value)
#      2. some data types are mutable, but others aren't
# So:

# If you pass a mutable object into a method, the method gets a reference to that same object and you can mutate it to your heart's delight, but if you rebind the reference in the method, the outer scope will know nothing about it, and after you're done, the outer reference will still point at the original object.

# If you pass an immutable object to a method, you still can't rebind the outer reference, and you can't even mutate the object.


def swap_bits(x, i, j):
    """Swaps bits at ith & jth positions in x
       Time complexity is O(1)
    """
    if (x >> i & 1) != (x >> j & 1):
        # bits at ith & jth index differ
        # swap their values by flipping indepent values
        # using mask
        mask = (1 << i) | (1 << j)
        x ^= mask

    return x




if __name__ == '__main__':
    print("Swap bits at ith & jth position")
    num = 1
    print("{:08b} -> swap bits at idx: 3 & idx:2 {:08b}".format(num, swap_bits(num, 3, 2)))
    num = 11
    print("{:08b} -> swap bits at idx: 3 & idx:2 {:08b}".format(num, swap_bits(num, 3, 2)))
    num = 19
    print("{:08b} -> swap bits at idx: 3 & idx:2 {:08b}".format(num, swap_bits(num, 3, 2)))
    num = 21
    print("{:08b} -> swap bits at idx: 3 & idx:2 {:08b}".format(num, swap_bits(num, 3, 2)))
    # swap_bits(num, 3, 2)
    # print("{:08b}".format(num))
