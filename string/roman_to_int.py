"""
罗马文转换成数字

https://leetcode.com/problems/roman-to-integer/
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        d, res = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}, 0
        for i in range(len(s) - 1):
            if d[s[i]] < d[s[i + 1]]:
                res -= d[s[i]]
            else:
                res += d[s[i]]
        res += d[s[-1]]
        return res


if __name__ == '__main__':
    arr = [1, 2, 3, 5, 4, 6]
    res = arr[-1]
    print(res)
