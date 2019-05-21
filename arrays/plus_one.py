"""
将数组的中的数字加一


https://leetcode.com/explore/learn/card/array-and-string/201/introduction-to-array/1148/
"""


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit = len(digits)
        num = sum([digits[i]*(10**(digit-i-1)) for i in range(digit)])+1
        return [int(i) for i in str(num)]


if __name__ == '__main__':
    nums = [9, 9, 9]
    res = Solution().plusOne(nums)
    print(res)
