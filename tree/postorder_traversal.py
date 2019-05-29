# Definition for a binary tree node.
from typing import List

"""
后序遍历

https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/930/
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        def aux(node):
            if node is None:
                return []
            return aux(node.left) + aux(node.right) + [node.val]
        return aux(root)
