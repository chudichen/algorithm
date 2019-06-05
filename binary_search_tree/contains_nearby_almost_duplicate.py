"""
判断是否满足nums[i]-nums[j]的绝对值小于等于t，i-j的绝对值小于等于k

https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/142/conclusion/1013/
"""


from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        ab = {}
        for i, num in enumerate(nums):
            if t <= k:
                for p in range(-t, t + 1):
                    if num + p in ab and abs(i - ab[num + p]) <= k: return True
            else:
                for key, val in ab.items():
                    if abs(key - num) <= t and abs(i - val) <= k: return True
            ab[num] = i
        return False


if __name__ == '__main__':
    arr = [1, 2, 3, 1]
    k = 3
    t = 0
    res = Solution().containsNearbyAlmostDuplicate(arr, k, t)
    print(res)
