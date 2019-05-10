"""
爬楼梯

依然fibonacci函数,climb_stairs为常规解，climb_stairsII为升级版，
不需要保存所有的值，只需要保存前一个的状态即可。

https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/1662/
"""


class Solution:
    def climb_stairs(self, n: int) -> int:
        cache = {0: 0, 1: 1, 2: 2}

        def calculation(num):
            if cache.get(num) is not None:
                return cache[num]
            res = calculation(num - 1) + calculation(num - 2)
            cache[num] = res
            return res

        return calculation(n)

    def climb_stairsII(self, n: int) -> int:
        cur = pre = 1
        for _ in range(n - 1):
            cur, pre = cur + pre, cur
        return cur


if __name__ == '__main__':
    result = Solution().climb_stairsII(5)
    print(result)
