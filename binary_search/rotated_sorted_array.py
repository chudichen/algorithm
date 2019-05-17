"""
在旋转子数组中查找目标值

依然是按照二分搜索的思路，有一半数据的有序的，如果刚好目标值在
这一块有序的区间内，就直接继续按照二分搜索的方式进行即可，如果
没有则继续所有查询返回。

https://leetcode.com/explore/learn/card/binary-search/125/template-i/952/
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if nums[mid] == target:
                return mid
            # 左边有序
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target <= nums[mid]:
                    hi = mid - 1
                else:
                    lo = mid + 1
            # 右边有序
            else:
                if nums[mid] <= target <= nums[hi]:
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1


if __name__ == '__main__':
    arr = [4, 5, 6, 7, 0, 1, 2]
    res = Solution().search(arr, 0)
    print(res)
