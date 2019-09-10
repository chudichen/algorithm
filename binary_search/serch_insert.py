"""
寻找下一个插入的位置

https://leetcode.com/problems/search-insert-position/
"""

from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        lo, hi = 0, len(nums)
        while lo <= hi:
            mid = (hi - lo) // 2 + lo
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                if mid == len(nums) - 1 or nums[mid + 1] > target:
                    return mid + 1
                else:
                    lo = mid + 1
            else:
                if mid == 0 or nums[mid - 1] < target:
                    return mid
                else:
                    hi = mid - 1


if __name__ == '__main__':
    nums = [1, 3]
    target = 0
    res = Solution().searchInsert(nums, target)
    print(res)
