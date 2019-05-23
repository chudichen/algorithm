"""
删除指定的元素

不能新建数组，要在原来的数组上进行操作，具体的实现原理是
使用双指针，将目标元素放在最后面。

https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1151/
"""
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        be, af, count = 0, len(nums) - 1, 0
        while be <= af:
            if nums[be] == val:
                nums[be], nums[af] = nums[af], nums[be]
                count += 1
                af -= 1
            else:
                be += 1
        return af + 1
