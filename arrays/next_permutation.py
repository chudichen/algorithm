"""
下一个排列

https://leetcode.com/problems/next-permutation/
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        leftmax = [0] * len(height)
        rightmax = [0] * len(height)
        s = 0
        m = 0
        for i in range(len(height)):
            m = max(m, height[i])
            leftmax[i] = m
        m = 0
        for j in range(1, len(height) + 1):
            m = max(m, height[-j])
            rightmax[-j] = m
        for i in range(len(height)):
            s += min(leftmax[i], rightmax[i]) - height[i]
        return s


if __name__ == '__main__':
    res = Solution().trap([0, 1])
    print(res)
