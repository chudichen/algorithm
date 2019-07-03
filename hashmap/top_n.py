"""
频率前n的元素

https://leetcode.com/explore/learn/card/hash-table/187/conclusion-hash-table/1133/
"""
import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = collections.Counter(nums).most_common(k)
        return [a[i][0] for i in range(k)]


if __name__ == '__main__':
    arr = [1, 1, 1, 2, 2, 3]
    k = 2
    res = Solution().topKFrequent(arr, 2)
    print(res)
