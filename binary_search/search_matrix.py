class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in matrix:
            if i[0] < target:
                l, r = 0, len(i) - 1
                while l <= r:
                    mid = l + (r - l) // 2
                    if i[mid] == target:
                        return True
                    if i[mid] > target:
                        r = mid - 1
                    else:
                        l = mid + 1
        return False


if __name__ == '__main__':
    arr = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
    target = 5
    res = Solution().searchMatrix(arr, target)
    print(res)
