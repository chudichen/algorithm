"""
三数字求和

https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/776/
"""
from typing import List


class Solution(object):
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set(tuple())
        nums.sort()
        for k in range(2, len(nums)):
            res = self.findTwoSum(nums, 0, k - 1, -nums[k], res)

        return res

    def findTwoSum(self, nums, i, j, target, res):
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                # a + b = -c
                res.add((nums[i], nums[j], -target))
                i += 1
                j -= 1
                while i < j and nums[i] == nums[i - 1]:
                    i += 1
                while i < j and nums[j] == nums[j + 1]:
                    j -= 1

        return res


if __name__ == '__main__':
    res = Solution().threeSum([-1, 0, 1, 2, -1, -4])
    print(res)
