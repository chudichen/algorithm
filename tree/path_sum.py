"""
路径的和

计算路径的和是否等于目标值，基本思路就是用递归遍历所有叶子节点。

https://leetcode.com/explore/learn/card/data-structure-tree/17/solve-problems-recursively/537/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        dif = sum - root.val
        if dif == 0 and root.left is None and root.right is None:
            return True
        left_value = self.hasPathSum(root.left, dif)
        right_value = self.hasPathSum(root.right, dif)
        return left_value or right_value
