# Definition for a binary tree node.
from typing import List
"""
中序后序重建二叉树

其实就是找到跟节点，然后剩余元素找到左右两个子节点

https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/943/
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if postorder:
            root_val = postorder.pop()
            root = TreeNode(root_val)
            index_of_root_val = inorder.index(root_val)
            root.left = self.buildTree(inorder[:index_of_root_val], postorder[:index_of_root_val])
            root.right = self.buildTree(inorder[index_of_root_val + 1:], postorder[index_of_root_val:])
            return root
