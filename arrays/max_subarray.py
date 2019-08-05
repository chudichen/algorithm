from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # For each element in the array, if the sum of element i-1 and element i is greater than element i,
        # assign element i the result of sum, otherwise, don't change element i.
        for i in range(1, len(nums)):
            nums[i] = max(nums[i - 1] + nums[i], nums[i])
        return max(nums)


if __name__ == '__main__':
    res = Solution().maxSubArray([-10, 1, 2, 3, -5])
    print(res)
