"""
验证二叉搜索树

利用二叉搜索树的特性，中序遍历为升序

https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/140/introduction-to-a-bst/997/
"""


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def inorder(root: TreeNode) -> List[int]:
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        res = inorder(root)
        i = 0
        for j in range(1, len(res)):
            if res[i] >= res[j]:
                return False
            i += 1
            j += 1
        return True
