# -*- coding: utf-8 -*-
"""
回文子字串，查找出回文子串。
其核心就是使用一个遍历加上一个回文比较，[i:j+1]可以获取到
需要比较的字符串，使用[::-1]进行反转。
https://leetcode.com/problems/palindromic-substrings/
"""


class Solution:
    def count_substrings(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        res = n
        for i in range(n):
            for j in range(i + 1, n):
                if s[i] == s[j] and s[i:j+1] == s[i: j+1][::-1]:
                    res += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    test_str = 'aaa'
    result = solution.count_substrings(test_str)
    print(result)
