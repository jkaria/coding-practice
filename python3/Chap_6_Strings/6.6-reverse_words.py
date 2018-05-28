#!/usr/local/bin/python3


def reverse_words(words):
    line = list(words)
    def reverse_range(s, e):
        while s < e:
            line[s], line[e] = line[e], line[s]
            s += 1
            e -= 1

    reverse_range(0, len(line)-1)

    s = e = 0
    while s < len(line):

        while e < len(line) and line[e].isalnum():
            e += 1

        reverse_range(s, e-1)
        s = e
        while s < len(line) and not line[s].isalnum():
            s += 1
        e = s

    return ''.join(line)


if __name__ == '__main__':
    print('Reverse words!')
    line = 'ram is costly'
    print('reverse_words({}) -> {}'.format(line, reverse_words(line)))
