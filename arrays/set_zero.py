"""
矩阵设置0

https://leetcode.com/problems/set-matrix-zeroes/
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        old_matrix = [x[:] for x in matrix]
        for y, row in enumerate(old_matrix):
            for x, cell in enumerate(row):
                if cell == 0:
                    for y2 in range(len(matrix)):
                        matrix[y2][x] = 0
                    matrix[y] = [0 for _ in range(len(row))]


if __name__ == '__main__':
    arr = [
        [0, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    Solution().setZeroes(arr)
    print(arr)
