#!/usr/local/bin/python3
import subprocess

def longest_zigzag(values):
    """Return len of the longest zigzag subsequence
    """
    if not values:
        return 0

    if len(values) == 1:
        return 1

    # if len(values) == 2:
    #     if values[0] == values[1]:
    #         return 1
    #     else:
    #         return 2

    maxLen = 1
    size = len(values)
    for idx in range(1, size):
        for idx2 in range(idx, size):
            subseq = [values[idx-1]]
            for val in values[idx2:]:
                if len(subseq) == 1:
                    if val < subseq[-1] or val > subseq[-1]:
                        subseq.append(val)
                    # print(subseq)
                    continue
                # now subseq has atleast 2 elems
                # print("evaluating {} for {}".format(val, subseq))
                if subseq[-1] - subseq[-2] > 0 and val - subseq[-1] < 0:
                    subseq.append(val)
                elif subseq[-1] - subseq[-2] < 0 and val - subseq[-1] > 0:
                    subseq.append(val)

            maxLen = max(maxLen, len(subseq))
        # if maxLen == len(subseq):
        #     print(subseq, len(subseq))
    return maxLen


def longest_zigzag_2(values):
    maxLen = 1
    up = [1]
    dwn = [1]
    for i in range(1, len(values)):
        up.append(1)
        dwn.append(1)
        for j in range(i):
            if values[i] > values[j]:
                up[i] = max(dwn[j]+1, up[i])
            if values[i] < values[j]:
                dwn[i] = max(up[j]+1, dwn[i])
        maxLen = max(maxLen, max(up[i], dwn[i]))
    return maxLen

def longest_zigzag_3(values):
    """Best solution O(N)"""
    if not values: # values is empty array
        return 0
    if len(values) == 1: # trival zigzag
        return 1
    directions = [values[i] - values[i-1] for i in range(1, len(values))]
    # print("len(values): {}, len(directions): {}, directions: {}".format(len(values),
    #                                                                     len(directions),
    #                                                                     directions))
    first_dir_idx = None
    for idx, dir in enumerate(directions):
        if dir:
            first_dir_idx = idx
            break

    if first_dir_idx == None:
        return 1

    maxLen = 2
    c_dir = directions[first_dir_idx]
    for idx in range(first_dir_idx+1, len(directions)):
        n_dir = directions[idx]
        if c_dir*n_dir < 0:
            maxLen +=1
            c_dir = n_dir

    return maxLen


if __name__ == '__main__':
    print('Zigzag problem!')
    # print(subprocess.check_output(['which', 'python3']))

    input1 = [10]
    print("res1: {:5} (expected: {})".format(longest_zigzag_3(input1), 1))
    input2 = [10, 20]
    print("res2: {:5} (expected: {})".format(longest_zigzag_3(input2), 2))
    input3 = [20, 10]
    print("res3: {:5} (expected: {})".format(longest_zigzag_3(input3), 2))
    input4 = [20, 20]
    print("res4: {:5} (expected: {})".format(longest_zigzag_3(input4), 1))
    input5 = [1, 17, 5, 10, 13, 15, 10, 5, 16, 8]
    print("res5: {:5}".format(longest_zigzag_3(input5)))
    input6 = [1, 2, 2, 1, 1, 2, 3, 3, 2, 1, 1, 2, 3, 4, 4, 3, 2, 1, 1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    print("res6: {:5} (expected: {})".format(longest_zigzag_3(input6), 9)) # 9
    input7 = [10, 9, 8, 7, 6, 7, 8, 9, 10]
    print("res7: {:5} (expected: {})".format(longest_zigzag_3(input7), 3))
    input8 = [12, 333, 700, 436, 1, 919, 959, 456, 456, 456, 1000, 193, 192, 13, 75, 818, 197, 197, 2, 777, 99, 81, 222, 109, 1000, 19, 27, 270, 62, 189, 987, 234, 55, 2, 718, 238, 901, 901, 900, 432, 55, 606, 89, 7, 7, 23, 789, 790, 800, 1000]
    print("res8: {:5} (expected: {})".format(longest_zigzag_3(input8), 26)) # 26
    input9 = [70, 55, 13, 2, 99, 2, 80, 80, 80, 80, 100, 19, 7, 5, 5, 5, 1000, 32, 32]
    print("res9: {:5} (expected: {})".format(longest_zigzag_3(input9), 8)) # 8
    input10 = [396, 549, 22, 819, 611, 972, 730, 638, 978, 342, 566, 514, 752, 871, 911, 172, 488, 542, 482, 974, 210, 474, 66, 387, 1, 872, 799, 262, 567, 113, 578, 308, 813, 515, 716, 905, 434, 101, 632, 450, 74, 254, 1000, 780, 633, 496, 513, 772, 925, 746]
    print("res10: {:5} (expected: {})".format(longest_zigzag_3(input10), 37)) # 37
    input11 = [61, 82, 126, 97, 167, 186, 119, 154, 155, 142, 153, 181, 172, 192, 223, 272, 273, 260, 280, 330, 329, 350, 273, 324, 349, 306, 385, 375, 420, 416, 435, 457, 373, 477, 395, 487, 500, 439, 493, 537, 518, 549, 542, 500, 524, 541, 512, 589, 549, 543]
    print("res11: {:5} (expected: {})".format(longest_zigzag_3(input11), 35)) # 35
