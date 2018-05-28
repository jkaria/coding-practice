#!/usr/local/bin/python3

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    m = len(nums1)
    n = len(nums2)
    if m > n:
        nums1, nums2 = nums2, nums1
        m, n = n, m

    # print("nums1: {}, nums2: {}".format(nums1, nums2))
    even = False if (m+n) % 2 else True

    if m == 0 or m < (m+n)//2:
        return 0.5*(nums2[(n-m)//2] + nums2[(n-m)//2 - 1]) if even else 1.0*nums2[(n-m)//2]

    if m == 1 and n == 1:
        return nums1[0] if nums1[0] < nums2[0] else nums2[0]

    i1 = 0
    i2 = 0
    while i1 + i2 < (m+n)//2:
        print('even: {}, i1: {}, i2: {}'.format(even, i1, i2))
        if nums1[i1] < nums2[i2]:
            i1 += (m - i1) // 2 if (m - i1) > 2 else 1
        else:
            i2 += (n - i2) // 2 if (n - i2) > 2 else 1

        # print('i1', i1, m-1, 'i2', i2, n-1)
        if i1 == m-1 or i2 == n-1:
            break

    median = 0

    if nums1[i1] < nums2[i2]:
        median += nums1[i1]
        if even:
            if i1+1 < m - 1 and nums1[i1+1] < nums2[i1]:
                median += nums1[i1+1]
            else:
                median += nums2[i2]
    else:
        median += nums2[i2]
        if even:
            if i2 + 1 < n - 1 and nums2[i2 + 1] < nums1[i1]:
                median += nums2[i2 + 1]
            else:
                median += nums1[i1]

    return median * 0.5 if even else median * 1.0


if __name__ == '__main__':
    print("Hello, World!")
    print("Welcome to Python3.0")
    a = [1, 5, 9, 21, 55]
    b = [3, 7, 20, 49, 69]
    print('findMedianSortedArrays({}, {}) -> {}'.format(a, b, findMedianSortedArrays(a, b)))

    a = [1, 2]
    b = [3, 4]
    print('findMedianSortedArrays({}, {}) -> {}'.format(a, b, findMedianSortedArrays(a, b)))

    a = [1, 3]
    b = [2]
    print('findMedianSortedArrays({}, {}) -> {}'.format(a, b, findMedianSortedArrays(a, b)))

    a = [1]
    b = []
    print('findMedianSortedArrays({}, {}) -> {}'.format(a, b, findMedianSortedArrays(a, b)))

    a = [2, 3]
    b = []
    print('findMedianSortedArrays({}, {}) -> {}'.format(a, b, findMedianSortedArrays(a, b)))


    a = [1]
    b = [2, 3, 4]
    print('findMedianSortedArrays({}, {}) -> {}'.format(a, b, findMedianSortedArrays(a, b)))

    a = [1]
    b = [1]
    print('findMedianSortedArrays({}, {}) -> {}'.format(a, b, findMedianSortedArrays(a, b)))
