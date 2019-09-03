"""
最长回文子串
回文的比较方法 a == a[::-1]

https://leetcode.com/problems/longest-palindromic-substring/
"""


class Solution(object):
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        res = ""
        for i in range(len(s)):
            sub_list = s[i:]
            while len(sub_list) > len(res):
                end_index = len(sub_list) - sub_list[::-1].index(sub_list[0])
                sub_list = sub_list[:end_index]

                if sub_list == sub_list[::-1]:
                    if len(sub_list) > len(res):
                        res = sub_list
                    break

                sub_list = sub_list[:-1]
        return res


if __name__ == '__main__':
    array = "abbaccca"
    res = Solution().longestPalindrome(array)
    print(res)
