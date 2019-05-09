"""
Pascal三角

保存前一个row的状态，计算下一行
https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/1660/
"""
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        arr = [1]
        for i in range(1, rowIndex + 1):
            arr_next = [1]
            for j in range(1, i):
                arr_next.append(arr[j] + arr[j - 1])
            arr_next.append(1)
            arr = arr_next
        return arr


if __name__ == '__main__':
    result = Solution().generate(6)
    print(result)
