#!/usr/local/bin/python3

MAPPING = ('0', '1', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ')


def find_mnemonics(num_str):
    res = []
    for n_chr in num_str:
        new_res = []
        for c in MAPPING[ord(n_chr) - ord('0')]:
            if res:
                for mn in res:
                    new_res.append(mn + c)
            else:
                new_res.append(c)
        res = new_res
    return res

def look_and_say(k):
    def next_num(s):
        res, i = [], 0
        while i < len(s):
            # print(i, s)
            cnt = 1
            c = s[i]
            while i + 1 < len(s) and c == s[i + 1]:
                cnt += 1
                i += 1
            res.append(str(cnt))
            res.append(str(c))
            i += 1
        return ''.join(res)

    num = '1'
    for _ in range(1, k):
        num = next_num(num)
        print(num)

    return num


if __name__ == '__main__':
    print('Find phone number mnemonics')
    print(find_mnemonics('23'), '->', len(find_mnemonics('23')), '(', len('23') * (3**len('23')), ')')
    print(find_mnemonics('234'), '->', len(find_mnemonics('234')), '(', len('234') * (3**len('234')), ')')
    print(find_mnemonics('2345'), '->', len(find_mnemonics('2345')), '(', len('2345') * (3**len('2345')), ')')
    print(look_and_say(8))

