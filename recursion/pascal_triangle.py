"""
Pascal三角

利用n=1为终止条件进行递归，后一项除了两边的元素外，其余元素值均为前一项的n+n-1
https://leetcode.com/explore/learn/card/recursion-i/251/scenario-i-recurrence-relation/1659/
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def helper(n):
            if n == 1:
                return [[1]]
            else:
                res = helper(n - 1)
                base = res[-1]
                cur = []
                for i in range(len(base) + 1):
                    if i == 0 or i == len(base):
                        cur += [1]
                    else:
                        cur += [base[i] + base[i - 1]]
                res.append(cur)
                return res
        if numRows == 0:
            return []
        return helper(numRows)


if __name__ == '__main__':
    result = Solution().generate(6)
    print(result)
