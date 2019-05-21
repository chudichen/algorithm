"""
对角线遍历

https://leetcode.com/explore/learn/card/array-and-string/202/introduction-to-2d-array/1167/
"""


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        dic = [[] for _ in range(len(matrix) + len(matrix[0]) - 1)]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i + j) % 2 == 0:
                    dic[i + j].insert(0, matrix[i][j])
                else:
                    dic[i + j].append(matrix[i][j])
        return [i for j in range(len(dic)) for i in dic[j]]


if __name__ == '__main__':
    nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    res = Solution().findDiagonalOrder(nums)
    print(res)
