"""
找到第k大的元素

使用python内置的堆排序可以轻松解决

https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/142/conclusion/1018/
"""
import heapq
import re
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = []
        self.k = k
        for i in nums:
            if len(self.arr) < k:
                heapq.heappush(self.arr, i)
            else:
                heapq.heappushpop(self.arr, i)

    def add(self, val: int) -> int:
        if len(self.arr) < self.k:
            heapq.heappush(self.arr, i)
        else:
            heapq.heappushpop(self.arr, i)
        return self.arr[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
