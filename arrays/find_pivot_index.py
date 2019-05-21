"""
寻找反转点

https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1144/
"""


class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
    """
        r = sum(nums)
        l = 0
        for i, x in enumerate(nums):
            if l == (r - l - x):
                return i
            l += x
        return -1


if __name__ == '__main__':
    nums = [-1, -1, -1, -1, -1, -1]
    res = Solution().pivotIndex(nums)
    print(res)
