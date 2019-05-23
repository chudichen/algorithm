"""
查询最长子数组

单指针即可，记录之前的长度
https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1301/
"""
from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sol, cur = 0, 0
        for i in nums:
            if i == 1:
                cur += 1
            else:
                sol = max(sol, cur)
                cur = 0
        return max(sol, cur)
