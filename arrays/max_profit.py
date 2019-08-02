class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # things I need from 'past' state would be the bought price...
        # things I need to deliver - maximum profit
        maxsum = float('-inf')
        if len(prices) == 0:
            return 0
        # you need the minimum of bought
        b = prices[0]
        for p in prices:
            # you need the maximum of profit
            if p - b > maxsum:
                maxsum = p - b
            # if it was useless with profit, maybe it could be a minimum bought price?
            if p < b:
                b = p
        return maxsum


if __name__ == '__main__':
    arr = [3, 2, 1, 4]
    res = Solution().maxProfit(arr)
    print(res)
