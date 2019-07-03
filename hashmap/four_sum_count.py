"""
计算四个值的和

https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1134/
"""
from typing import List


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ans = 0
        sum_ab = {}
        for a in A:
            for b in B:
                anb = a+b
                if anb in sum_ab:
                    sum_ab[anb] += 1
                else:
                    sum_ab[anb] = 1
        for c in C:
            for d in D:
                if -c-d in sum_ab:
                    ans += sum_ab[-c-d]
        return ans


if __name__ == '__main__':
    a = [1, 2]
    b = [-2, -1]
    c = [-1, 2]
    d = [0, 2]
    res = Solution().fourSumCount(a, b, c, d)
    print(res)
