"""
旋转遍历矩阵

https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1168/
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        top, bottom, left, right = 0, len(matrix), 0, len(matrix[0])
        cur = 0
        res = []
        while top < bottom and left < right:
            if cur == 0:
                res += [matrix[top][i] for i in range(left, right)]
                cur = 1
                top += 1
            elif cur == 1:
                res += [matrix[i][right - 1] for i in range(top, bottom)]
                cur = 2
                right -= 1
            elif cur == 2:
                res += [matrix[bottom - 1][i] for i in range(right - 1, left - 1, -1)]
                cur = 3
                bottom -= 1
            else:
                res += [matrix[i][left] for i in range(bottom - 1, top - 1, -1)]
                cur = 0
                left += 1
        return res


if __name__ == '__main__':
    m = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    res = Solution().spiralOrder(m)
    print(res)
