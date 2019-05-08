# -*- coding: utf-8 -*-
"""
由重复子串组成的字符串

子串乘以位数是否与目标字符串相等
https://leetcode.com/problems/repeated-substring-pattern/
"""


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                sub_str = s[:i]
                if sub_str * (n // i) == s:
                    return True
        return False


if __name__ == '__main__':
    solution = Solution()
    res = solution.repeatedSubstringPattern("aba")
    print(res)
