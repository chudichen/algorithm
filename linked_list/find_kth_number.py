"""
You will notice that for row N, the first half will be exact same with the row N-1, and the second half is the mirror of first half (0 to 1, 1 to 0)

So if you look for Kth element at Row N,

Total : 2^(N-1) elements
val(N, K) = Kth element at Row N-1 if K in first 2^N-2 elements
OR
val(N, K) = val(N-1, K-2^(N-2)) if K is in 2nd half
"""


class Solution(object):
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        return self.findKthNumber(N, K)

    def findKthNumber(self, N, K):

        if N >= 2:
            if K <= 2 ** (N - 2):
                return self.findKthNumber(N - 1, K)
            else:
                if self.findKthNumber(N - 1, K - 2 ** (N - 2)) == 0:
                    return 1
                else:
                    return 0
        elif N == 1:
            if K == 1:
                return 0
            elif K == 2:
                return 1
        elif N == 0:
            if K == 1:
                return 0
