"""



https://leetcode.com/explore/interview/card/top-interview-questions-medium/109/backtracking/793
"""
from typing import List


class Solution:
    def __init__(self):
        self.lookup = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        return self.singleletter('', digits, 0)

    def singleletter(self, s: str, digits: str, n: int) -> List[str]:
        if n == len(digits):
            return [s]

        element = self.lookup[digits[n]]
        res = []
        for i in element:
            res += self.singleletter(s + i, digits, n + 1)
        return res


if __name__ == '__main__':
    res = Solution().letterCombinations("56")
    print(res)
