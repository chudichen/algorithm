from typing import List
"""
获取并集

先排序，然后利用二分查找法进行查找，然后移除找到的元素,
也有取巧的方法，直接利用set，python的库太强大了

https://leetcode.com/explore/learn/card/binary-search/144/more-practices/1034/
"""


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = set(nums1)
        b = set(nums2)
        c = a & b
        return list(c)
