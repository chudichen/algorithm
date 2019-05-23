"""
寻找目标和的最小子串

利用双指针来维护一个连续子串，并计算子串的和

https://leetcode.com/explore/learn/card/array-and-string/205/array-two-pointer-technique/1299/
"""
from typing import List


class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        i, count, size = 0, 0, 0

        for j in range(len(nums)):
            count += nums[j]
            if count >= s:
                while count >= s:
                    count -= nums[i]
                    i += 1
                size = j - i + 2 if size == 0 else min(size, j - i + 2)

        return size


if __name__ == '__main__':
    target = 7
    arr = [2, 3, 1, 2, 4, 3]
    res = Solution().minSubArrayLen(target, arr)
    print(res)
