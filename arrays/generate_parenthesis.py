"""
生成所有的括号组合

本题采用回溯（Backtracking）的思想：在当前局面下，你有若干种选择。那么尝试每一种选择。
如果已经发现某种选择肯定不行（因为违反了某些限定条件），就返回；如果某种选择试到最后
发现是正确

https://leetcode.com/problems/generate-parentheses/
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(combination, op_count, cl_count, counter):
            if cl_count == 0:
                res.append(combination)
            else:
                # when op_count > 0 add '(' and decrement op_count, increment counter
                if op_count > 0:
                    generate(combination + '(', op_count - 1, cl_count, counter + 1)
                    # add ')' only if counter > 0 (implying that there is an unbalanced opening bracket),
                    # decrement cl_count and decrement counter
                if counter > 0:
                    generate(combination + ')', op_count, cl_count - 1, counter - 1)

        res = []
        generate("", n, n, 0)
        return res


if __name__ == '__main__':
    res = Solution().generateParenthesis(3)
    print(res)
