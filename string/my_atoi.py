"""
将字符串转为数字

https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/
"""


class Solution:
    INT_MAX = 2 ** 31 - 1
    INT_MIN = -2 ** 31

    def get_start_idx(self, text: str) -> int:
        start_idx = 0
        for i, char in enumerate(text):
            if char != ' ':
                return start_idx
            start_idx += 1
        return start_idx

    def myAtoi(self, text: str) -> int:
        if not text:
            return 0

        start_idx = self.get_start_idx(text)

        if start_idx >= len(text):
            return 0

        sign = text[start_idx] in ['-', '+']

        if text[start_idx].isalpha() or (sign and len(text) == 1):
            return 0

        value = ''
        start = start_idx + 1 if sign else start_idx

        for i in range(start, len(text)):
            char = text[i]

            if not char.isnumeric():
                if not value:
                    return 0
                break
            value += char

        value = int(value)
        if sign and text[start_idx] == '-':
            value = max(-1 * value, Solution.INT_MIN)
        else:
            value = min(value, Solution.INT_MAX)

        return value


if __name__ == '__main__':
    s = "-111 test"
    res = Solution().myAtoi(s)
    print(res)
