"""
计算二进制

可以直接使用python库方法进行二进制换算

https://leetcode.com/explore/learn/card/array-and-string/203/introduction-to-string/1160/
"""


class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    s1 = '1'
    s2 = '110'
    print(int(s1, 2))
