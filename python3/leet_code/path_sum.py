#!/usr/local/bin/python3
import collections
import re


def pathSum(root, sum):
    """
    :type root: TreeNode
    :type sum: int
    :rtype: List[List[int]]
    """
    res = []
    q = collections.deque([(root, root.val, [root.val])])
    while q:
        print(q)
        node, sum_so_far, path = q.popleft()
        if node.left is None and node.right is None and sum_so_far == sum:
            res.append(path + [node.val])
        if node.left:
            q.append((node.left, sum_so_far + node.val, path + [node.val]))
        if node.right:
            q.append((node.right, sum_so_far + node.val, path + [node.val]))

    return res


def mostCommonWord(paragraph, banned):
    """
    :type paragraph: str
    :type banned: List[str]
    :rtype: str
    """
    counter = {}
    for word in paragraph.split(' '):
        m = re.match("([a-z]+)", word.lower())
        if m:
            w = m.group(1)
            if w not in banned:
                if w not in counter:
                    counter[w] = 0
                counter[w] += 1

    res, cnt = None, 0
    for item in counter.items():
        if item[1] > cnt:
            res, cnt = item[0], item[1]

    return res


def ambiguous_coordinates(S):
    def generate_permutations(s):
        # print(s)
        if s == '0':
            return [s]
        if s[0] == '0':
            if s.rfind('0') == len(s) - 1: # all 0's
                return []
            else:
                # print(s[1:])
                return ['0.' + s[1:]]

        combs = [s]
        if s[-1] != '0':
            for i in range(1, len(s)):
                combs.append(s[:i] + '.' + s[i:])
        return combs

    res = []
    for i in range(2, len(S) - 1):
        x_combs = generate_permutations(S[1:i])
        y_combs = generate_permutations(S[i:len(S) - 1])
        for x in x_combs:
            for y in y_combs:
                res.append("({}, {})".format(x, y))
    return res


def racecar(target):
    """
    :type target: int
    :rtype: int
    """
    pos, speed, inst = 0, 1, []
    while True:
        print('pos:', pos, 'speed:', speed)
        if pos == target:
            break
        if pos < target:
            if speed > 0:
                if speed/2 >= target - pos:
                    inst.append('R')
                    inst.append('R')
                    speed = 1
                inst.append('A')
                pos += speed
                speed *= 2
            else:
                inst.append('R')
                speed = speed/abs(speed) * -1
        else: # pos > target
            if speed < 0:
                if abs(speed/2) >= pos - target:
                    inst.append('R')
                    inst.append('R')
                    speed = -1
                inst.append('A')
                pos += speed
                speed *= 2
            else:
                inst.append('R')
                speed = speed/abs(speed) * -1


    return len(inst)

if __name__ == '__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(mostCommonWord(paragraph, banned))

    # S = "(123)"
    # print(ambiguous_coordinates(S))
    S = "(00011)"
    print(ambiguous_coordinates(S))
    S = "(0123)"
    print(ambiguous_coordinates(S))
    S = "(100)"
    print(ambiguous_coordinates(S))
    # Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]

    print(racecar(5))

