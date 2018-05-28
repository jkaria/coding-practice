#!/urs/local/bin/python3


def isInterleave(s1, s2, s3):
    """
    :type s1: str
    :type s2: str
    :type s3: str
    :rtype: bool
    """
    def match_prefix(s1, s2, s3):
        # print(s1, s2, s3)
        if not s3:
            return not s1 and not s2
        elif "{}-{}".format(s1, s2) in false_combinations:
            return False
        elif s1 and s3[0] == s1[0] and match_prefix(s1[1:], s2, s3[1:]):
            return True
        elif s2 and s3[0] == s2[0] and match_prefix(s1, s2[1:], s3[1:]):
            return True
        else:
            false_combinations.add("{}-{}".format(s1, s2))
            return False

    false_combinations = set()
    return match_prefix(s1, s2, s3)


if __name__ == '__main__':
    print('S3 is formed by interleaving S1 and S2?')

    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(isInterleave(s1, s2, s3))
