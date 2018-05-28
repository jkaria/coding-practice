#!/usr/local/bin/python3
import collections


def can_string_be_a_palindrome(s):
    if len(s) == 1:
        return True

    arr = sorted(s)
    return all( arr[2*i] == arr[2*i + 1] for i in range( len(arr) % 2))


def can_string_be_a_palindrome_using_counter(s):
    """ Time complexity = O(n) n is number of chars in s
        Space complexity = O(c) c is unique chars in s
    """
    print(collections.Counter(s))
    return sum( x % 2 for x in collections.Counter(s).values() ) <= 1


if __name__ == '__main__':
    print('Test for palindromic permutations in a string!')

    can_string_be_a_palindrome = can_string_be_a_palindrome_using_counter

    s = 'a'
    print("can_string_be_a_palindrome({}) -> {}".format(s, can_string_be_a_palindrome(s)))

    s = 'abc'
    print("can_string_be_a_palindrome({}) -> {}".format(s, can_string_be_a_palindrome(s)))

    s = 'abcabc'
    print("can_string_be_a_palindrome({}) -> {}".format(s, can_string_be_a_palindrome(s)))

    s = 'deified'
    print("can_string_be_a_palindrome({}) -> {}".format(s, can_string_be_a_palindrome(s)))
