#!/usr/local/bin/python3


def kEmptySlots(flowers, k):
    """
    :type flowers: List[int]
    :type k: int
    :rtype: int
    """
    bloom_status = [0] * (len(flowers) + 1)
    for day, flower_idx in enumerate(flowers, 1):
        print("day:", day, "flower_idx:", flower_idx)
        bloom_status[flower_idx] = 1
        offset = 1
        violated = False
        while not violated and offset <= k:
            l_idx = flower_idx - offset
            if l_idx > 0 and bloom_status[l_idx]:
                violated = True
                continue
            u_idx = flower_idx + offset
            if u_idx < len(flowers) and bloom_status[u_idx]:
                violated = False
                continue
            offset += 1

        if not violated:
            l_idx, u_idx = flower_idx - offset, flower_idx + offset
            if (l_idx > 0 and bloom_status[l_idx]) or (u_idx < len(flowers) and bloom_status[u_idx]):
                return day

    return -1


def nextClosestTime(time):
    """
    :type time: str
    :rtype: str
    """
    m = re.match("([0-9]{1})([0-9]{1}):([0-9]{1})([0-9]{1})", time)
    digits = set([int(m.group(i)) for i in range(1, 5)])
    in_mins = (int(m.group(1))*10 + int(m.group(2))) * 60 + (int(m.group(3))*10 + int(m.group(4)))
    for nxt_min in range(in_mins + 1, 24*60):
        hr, mins = nxt_min // 60, nxt_min % 60
        print(nxt_min, hr, mins)
        new_digits = set([hr//10, hr%10, mins//10, mins%10])
        if not digits - new_digits:
            return "{}:{}".format(hr, mins)

    min_digit = sorted(digits)[0]
    return "{}{}:{}{}".format(min_digit, min_digit, min_digit, min_digit)


def lengthOfLongestSubstringKDistinct(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    last_seen_at = {}
    s_idx = 0
    distinct_chars = set()
    max_substr_size = 0
    for idx, c in enumerate(s):
        print(idx, c)
        last_seen_at[c] = idx
        if c not in distinct_chars:
            if len(distinct_chars) == k:
                last_idxes = sorted([(last_seen_at[d_c], d_c) for d_c in distinct_chars])
                left_most_idx, left_most_char = last_idxes[0]
                print("--", left_most_idx, left_most_char)
                distinct_chars.remove(left_most_char)
                s_idx = left_most_idx + 1
            distinct_chars.add(c)
        print('-', max_substr_size, idx - s_idx - 1)
        max_substr_size = max(max_substr_size, idx - s_idx + 1)

    return max_substr_size


if __name__ == '__main__':
    print(kEmptySlots([1,3,2], 1))
    print(lengthOfLongestSubstringKDistinct("eceba", 2))
