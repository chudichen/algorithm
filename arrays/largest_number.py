"""
找到最大数并且最大数要是其他数的两倍

https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1147/
"""


class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m = max(nums)
        t = None
        for i in range(len(nums)):
            if nums[i] == max:
                t = i
            if i != t and nums[i] * 2 > m:
                return -1
        return t


if __name__ == '__main__':
    nums = [0,0,0,1]
    res = Solution().dominantIndex(nums)
    print(res)
