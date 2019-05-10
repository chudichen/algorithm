"""
斐波那契函数

使用缓存来提速，这个技术叫做Memoization
https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/1661/
"""


class Solution:
    def fib(self, N: int) -> int:
        cache = {0: 0, 1: 1}

        def calculation(num):
            if cache.get(num) is not None:
                return cache[num]
            else:
                res = calculation(num - 2) + calculation(num - 1)
                cache[num] = res
                return res

        return calculation(N)


if __name__ == '__main__':
    result = Solution().fib(5)
    print(result)
