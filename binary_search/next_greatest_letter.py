"""
找出下一个字母

值得注意的点就是while l <= r:当使用<=的时候 游标是可以取得到最右边的点

https://leetcode.com/explore/learn/card/binary-search/137/conclusion/977
"""
from typing import List


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if letters[mid - 1] <= target < letters[mid]:
                return letters[mid]
            elif letters[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return letters[0]


if __name__ == '__main__':
    letter_list = ["c", "f", "j"]
    res = Solution().nextGreatestLetter(letter_list, 'g')
    print(res)
