"""
最长子回文

https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/780/
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_length = len(s)
        if s_length <= 1:
            return s

        answer = s[0]

        for i in range(s_length - 1):
            # end early
            if (len(answer) >= 2 * i + 1) or (len(answer) >= 2 * (s_length - i - 1) + 1):
                continue

            # center: one character
            for j in range(1, i + 2):
                if (j > i) or (i + j + 1 > s_length) or (s[i - j] != s[i + j]):
                    if 2 * j - 1 > len(answer):
                        answer = s[i - j + 1:i + j]
                    break

            if s[i + 1] == s[i]:
                # center: two character
                for j in range(1, i + 2):
                    if (j > i) or (i + j + 2 > s_length) or (s[i - j] != s[i + j + 1]):
                        if 2 * j > len(answer):
                            answer = s[i - j + 1:i + j + 1]
                        break
        return answer


if __name__ == '__main__':
    res = Solution().longestPalindrome("abbaaa")
    print(res)
    # test_arr = [1, 2, 3, 5, 4, 6]
    # s_length = len(test_arr)
    # for i in range(s_length - 1):
    #     print(2 * (s_length - i - 1) + 1)
