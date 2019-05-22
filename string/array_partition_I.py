"""
数组分区

将每两个数字分为一组，取出最小值，然后计算总和。
核心解题思路在于当一个较大数和一个较小的数组合在一起的时候，那个较小的数字就被浪费了
因此先进行排序，将相邻的两个数组合在一起。

https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1154/
"""


class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(sorted(nums)[::2])


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    for i in arr[::2]:
        print(i)
