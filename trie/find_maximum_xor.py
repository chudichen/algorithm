"""


https://leetcode.com/explore/learn/card/trie/149/practical-application-ii/1057/
"""
from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        def select_bit(num, pos):
            # 0 indexed pos
            return (num >> pos) % 2

        def foo(up, dn, pos):
            if pos < 0:
                return up[0] ^ dn[0]

            up1 = [x for x in up if select_bit(x, pos) == 0]
            dn1 = [x for x in dn if select_bit(x, pos) == 1]

            up2 = [x for x in up if select_bit(x, pos) == 1]
            dn2 = [x for x in dn if select_bit(x, pos) == 0]

            has_split1 = len(up1) > 0 and len(dn1) > 0
            has_split2 = len(up2) > 0 and len(dn2) > 0

            if not has_split1 and not has_split2:
                return foo(up, dn, pos - 1)

            val1, val2 = None, None
            if has_split1:
                val1 = foo(up1, dn1, pos - 1)
            if has_split2:
                val2 = foo(up2, dn2, pos - 1)

            if val1 != None and val2 != None:
                val = max((val1, val2))
            elif val1 != None:
                val = val1
            else:
                val = val2

            return val

        has_diff = False  # has different numbers
        for pos in range(30, -1, -1):
            up = [x for x in nums if select_bit(x, pos) == 0]
            dn = [x for x in nums if select_bit(x, pos) == 1]
            if len(up) > 0 and len(dn) > 0:
                has_diff = True
                break

        if has_diff:
            return foo(up, dn, pos - 1)
        else:
            return 0
