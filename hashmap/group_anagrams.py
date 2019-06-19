"""
单词分类

https://leetcode.com/explore/learn/card/hash-table/185/hash_table_design_the_key/1124/
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            index = ''.join(sorted(s))
            if index not in anagrams:
                anagrams[index] = []
            anagrams[index].append(s)
        return sorted(anagrams.values())
