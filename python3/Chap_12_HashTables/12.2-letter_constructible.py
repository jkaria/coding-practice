#!/usr/local/bin/python3
import collections


def is_anonymous_letter_constructible_from_magazine(letter_text, magazine_text):
    """ Time complexity -> O(m+n) where m=chars in magazine_text & n chars in letter_text
        Space complexity -> O(L) where L is uniq chars in letter_text
        NOTE: if chars are ASCII encoded then hash table can be substited for
              an array A of size 256 and A[i] represents the char count in letter
    """
    letter_text_freq = collections.Counter(letter_text)

    for char in  magazine_text:
        if char in letter_text_freq:
            letter_text_freq[char] -= 1
            if not letter_text_freq[char]:
                letter_text_freq.pop(char)
                if not letter_text_freq:
                    return True
    return not letter_text_freq


def is_anonymous_letter_constructible_from_magazine_pythonic(letter_text, magazine_text):
    return not collections.Counter(letter_text) - collections.Counter(magazine_text)


if __name__ == '__main__':
    print('Determine if an anonymous letter is constructible from magazine')

    letter_text = 'abcdefgh'
    magazine_text = 'aabccdeefgh'
    print('is_anonymous_letter_constructible_from_magazine({}, {}) -> {}'
          .format(letter_text,
                  magazine_text,
                  is_anonymous_letter_constructible_from_magazine_pythonic(letter_text,
                                                                           magazine_text)
                  )
          )
