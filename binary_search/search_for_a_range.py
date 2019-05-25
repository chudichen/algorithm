"""
搜索一个范围内的数字

二分法先查找到目标值，然后再向左和向右找到该值的边界。

https://leetcode.com/explore/learn/card/binary-search/135/template-iii/944/
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r, t = 0, len(nums) - 1, -1
        # 查找到目标值
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                t = mid
                break
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        if t == -1:
            return [-1, -1]

        s, e = t, t
        # 左边界
        while s >= 0 and nums[s] == target:
            s -= 1
        s += 1
        # 右边界
        while e < len(nums) and nums[e] == target:
            e += 1
        e -= 1
        return [s, e]
