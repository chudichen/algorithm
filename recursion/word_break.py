"""
拆分单词

https://leetcode.com/problems/word-break
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s in wordDict:
            return True

        cache = {}

        def wb(word: str, index: int) -> bool:
            if len(word) < index:
                return False

            result = False
            if word[:index] in wordDict:
                if word[index:] in wordDict:
                    return True
                elif word[index:] in cache:
                    result = cache[word[index:]]
                else:
                    result = wb(word[index:], 0)
                    cache[word[index:]] = result
            return result or wb(word, index + 1)

        return wb(s, 1)
