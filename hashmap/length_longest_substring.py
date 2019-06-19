class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = end = max_len = 0
        while end < len(s):
            if s[end] in s[start: end]:
                start += 1
            else:
                end += 1
            max_len = max(end - start, max_len)
        return max_len


if __name__ == '__main__':
    res = Solution().lengthOfLongestSubstring(" ")
    print(res)
