#!/usr/local/bin/python3


def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    can_jump_tracker = {}

    def can_cross_helper(j_idx, last_jump):
        print('helper ->', j_idx, last_jump)
        itr_key = '{}_{}'.format(j_idx, last_jump)
        if j_idx == len(stones):
            can_jump_tracker[itr_key] = True
            return True

        if itr_key in can_jump_tracker:
            return can_jump_tracker[itr_key]

        for i in range(j_idx + 1, len(stones)):
            new_jump = stones[i] - stones[j_idx]
            # print('       i ->', i, 'new_jump:', new_jump, 'last_jump:', last_jump)
            if new_jump < last_jump - 1:
                continue
            if new_jump > last_jump + 1:
                break
            if can_cross_helper(i, new_jump):
                can_jump_tracker[itr_key] = True
                return True
        print('-----', itr_key)
        can_jump_tracker[itr_key] = False
        return False


    return can_cross_helper(0, 0)


if __name__ == '__main__':
    print('can frog cross the river!')

    a = [0,1,3,5,6,8,12,17]
    print('canCross({}) -> {}'.format(a, canCross(a)))

    # a = [0,1,2,3,4,8,9,11]
    # print('canCross({}) -> {}'.format(a, canCross(a)))

    # a = [0,1,3,4,5,7,9,10,12]
    # print('canCross({}) -> {}'.format(a, canCross(a)))
