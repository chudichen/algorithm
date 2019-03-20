# -*- coding: utf-8 -*-
"""
经典的快速排序算法，利用前后指针确定基准值的位置，并使用遍历
对剩余的元素进行排序,虽然思路简单，但是要注意边界的处理。
"""


# 快速排序
class Solution:
    def quick_sort(self, arr, left, right):
        if left <= right:
            # 初始化标准值，左指针，右指针
            base, lo, hi = arr[left], left, right
            while lo < hi:
                # 从右开始找到第一个小于base的位置
                while base <= arr[hi] and lo < hi:
                    hi -= 1
                arr[lo] = arr[hi]
                # 从左开始找到第一个大于base的位置
                while base >= arr[lo] and lo < hi:
                    lo += 1
                arr[hi] = arr[lo]
            arr[lo] = base
            self.quick_sort(arr, left, lo - 1)
            self.quick_sort(arr, lo + 1, right)


# 测试方法
if __name__ == '__main__':
    test_arr = [6, 8, 1, 4, 3, 9, 5, 4, 11, 2, 2, 15, 6]
    print('Before quick sort array is: ' + str(test_arr))
    solution = Solution()
    solution.quick_sort(test_arr, 0, len(test_arr) - 1)
    print('After quick sort array is: ' + str(test_arr))

