"""
前序遍历二叉树

节点的顺序是中左右,如果使用遍历代替递归执行速度会快一些。

https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928
"""


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        def aux(node):
            if not node:
                return []
            return [node.val] + aux(node.left) + aux(node.right)
        return aux(root)

