# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        def guess(t):
            a = 1
            if t == a:
                return 0
            if t > a:
                return 1
            else:
                return -1
        l, r = 0, n
        while l < r:
            mid = l + (r - l) // 2
            res = guess(mid)
            if res == 0:
                return mid
            if res == 1:
                r = mid
            else:
                l = mid + 1
        return -1


if __name__ == '__main__':
    res = Solution().guessNumber(1)
    print(res)
