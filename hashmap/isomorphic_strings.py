"""
同构字符串

判断是否是同构字符串

https://leetcode.com/explore/learn/card/hash-table/184/comparison-with-other-data-structures/1117/
"""


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        iso = {}
        if len(s) != len(t):
            return False
        for i, char in enumerate(s):
            if char not in iso.keys() and not t[i] in iso.values():
                iso[char] = t[i]
            else:
                if char not in iso.keys() or t[i] not in iso.values():
                    return False
                if iso[char] != t[i]:
                    return False
        return True


if __name__ == '__main__':
    res = Solution().isIsomorphic('egg', 'add')
    print(res)
