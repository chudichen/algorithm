"""
子串的和等于目标值

https://leetcode.com/problems/subarray-sum-equals-k/
"""

from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, p, d = 0, 0, {0: 1}
        for i in nums:
            p += i
            if p - k in d: count += d[p - k]
            d[p] = d.setdefault(p, 0) + 1
        return count


if __name__ == '__main__':
    nums = [1, 1, 1]
    k = 2
    res = Solution().subarraySum(nums, k)
    assert res == 2
