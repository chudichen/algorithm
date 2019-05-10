"""
查找二叉树最大深度

核心在于递归条件的编写，可以想象成是从二叉树叶子节点开始计数的

https://leetcode.com/explore/learn/card/recursion-i/256/complexity-analysis/2375/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
