# Definition for a binary tree node.
from typing import List
"""
中序遍历二叉树

https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/929/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            if node is None:
                continue
            if type(node) is int:
                res += [node]
            else:
                stack += [node.right] + [node.val] + [node.left]
        return res
