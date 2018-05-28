#!/usr/local/bin/python3


def is_palindromic(word):
    return all(word[i] == word[~i] for i in range(0, len(word)//2) )

def count_substrings(s):
    """
    :type s: str
    :rtype: int
    """
    def is_palindrome(s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

    num_substrs = 0
    for center in range(2 * len(s)):
        left = center // 2
        right = left + center % 2
        while( left >= 0 and right < len(s) and s[left] == s[right]):
            num_substrs += 1
            left -= 1
            right += 1

    return num_substrs


if __name__ == '__main__':
    print("Test if a string is pallindrome!")

    # print("is_palindromic('{}') -> {}".format("a", is_palindromic("a")))
    # print("is_palindromic('{}') -> {}".format("aa", is_palindromic("aa")))
    # print("is_palindromic('{}') -> {}".format("ab", is_palindromic("ab")))
    # print("is_palindromic('{}') -> {}".format("abcba", is_palindromic("abcba")))
    # print("is_palindromic('{}') -> {}".format("abcde", is_palindromic("abcde")))
    print("count_substrings('aaaaa') ->", count_substrings('aaaaa'))
