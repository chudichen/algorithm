from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0

        current_best_cost = prev_best_cost = 0

        for val in nums:
            if val + prev_best_cost > current_best_cost:
                prev_best_cost, current_best_cost = current_best_cost, val + prev_best_cost

            else:
                prev_best_cost = current_best_cost

        return current_best_cost


if __name__ == '__main__':
    res = Solution().rob([2, 1, 1, 1, 2])
    print(res)
