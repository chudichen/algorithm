"""
数字转罗马文

https://leetcode.com/problems/integer-to-roman/
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ''
        symb = ['I', 'V', 'X', 'L', 'C', 'D', 'M']

        digit = []
        while num > 0:
            digit += [num % 10]
            num = int((num - num % 10) / 10)

        for i in range(len(digit)):
            if digit[i] == 0:
                roman = '' + roman
            if digit[i] < 4:
                roman = symb[2 * i] * (digit[i]) + roman
            if digit[i] == 4:
                roman = symb[2 * i] + symb[2 * i + 1] + roman
            if digit[i] == 5:
                roman = symb[2 * i + 1] + roman
            if 9 > digit[i] > 5:
                roman = symb[2 * i + 1] + symb[2 * i] * (digit[i] - 5) + roman
            if digit[i] == 9:
                roman = symb[2 * i] + symb[2 * i + 2] + roman

        return roman


if __name__ == '__main__':
    res = Solution().intToRoman(14)
    print(res)
