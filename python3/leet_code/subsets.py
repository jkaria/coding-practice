#!/usr/local/bin/python3



def subsets(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    def subset_helper(idx, subset_so_far):
        if idx == len(nums):
            res.append([i for i in subset_so_far if i is not None])
        else:
            cnt = 1
            while idx < len(nums) - 1 and nums[idx] == nums[idx + 1]:
                cnt += 1
                idx += 1
            subset_helper(idx + 1, subset_so_far + [None]) # without this number
            subset_helper(idx + 1, subset_so_far + [nums[idx]]) # with this number
            if cnt > 1:
                for c in range(2, cnt + 1):
                    subset_helper(idx + 1, subset_so_far + [nums[idx]] * c)

    res = []
    subset_helper(0, [])
    return res


if __name__ == '__main__':
    print(subsets([1, 2, 2]))
    print(subsets([5, 5, 5, 5, 5]))
