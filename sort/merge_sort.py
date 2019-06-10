from typing import List
"""
归并排序

采用分而治之的思想，先拆成单个，两两进行排序，然后再合并结果
https://leetcode.com/explore/learn/card/recursion-ii/470/divide-and-conquer/2944/
"""


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # bottom cases: empty or list of a single element.
        if len(nums) <= 1:
            return nums

        pivot = len(nums) // 2
        left_list = self.sortArray(nums[0:pivot])
        right_list = self.sortArray(nums[pivot:])
        return self.merge(left_list, right_list)

    def merge(self, left_list, right_list):
        res = []
        while left_list and right_list:
            res += [left_list.pop(0)] if left_list[0] < right_list[0] else [right_list.pop(0)]

        res += left_list
        res += right_list
        return res


if __name__ == '__main__':
    nums = [5, 2, 3, 1]
    res = Solution().sortArray(nums)
    assert res == sorted(nums)
    print(res)
