"""
最小公共索引

https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1177/
"""
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        n = float("inf")
        best = []
        for ind1, each in enumerate(list1):
            if each in list2:
                ind2 = list2.index(each)
                if ind1 + ind2 <= n:
                    best.append(each)
                    n = ind1 + ind2
        return best
