from typing import List


class Solution(object):
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        cur_sum = sum([num for num in A if not num & 1])
        res = []
        for val, idx in queries:
            if A[idx] & 1 and val & 1:
                cur_sum += A[idx] + val
            elif not A[idx] & 1 and val & 1:
                cur_sum -= A[idx]
            elif not A[idx] & 1 and not val & 1:
                cur_sum += val
            A[idx] += val
            res.append(cur_sum)
        return res


if __name__ == '__main__':
    A = [1, 2, 3, 4]
    queries = [[1, 1], [-3, 1], [-4, 1], [2, 1]]
    res = Solution().sumEvenAfterQueries(A, queries)
    print(res)
