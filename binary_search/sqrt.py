"""
开根号

开根号并保留整数位
https://leetcode.com/explore/learn/card/binary-search/125/template-i/950/
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x
        while l <= r:
            mid = l + (r-l) // 2
            sq = mid*mid
            tem = mid*mid*mid
            if sq <= x <= tem:
                return mid
            if x < sq:
                r = mid
            else:
                l = mid + 1


if __name__ == '__main__':
    res = Solution().mySqrt(9)
    print(res)
