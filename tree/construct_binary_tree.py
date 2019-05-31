"""
重建二叉树

根据前序遍历以及中序遍历重建二叉树,前序遍历是中左右，中序遍历左中右。
用前序遍历确定中间的位置，中序遍历确定左右两侧的位置。
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def build_tree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def buildNode(i, j):
            if i == j:
                return None
            parent = TreeNode(preorder.pop(0))
            split_index = inorder.index(parent.val)
            parent.left = buildNode(i, split_index)
            parent.right = buildNode(split_index + 1, j)
            return parent
        return buildNode(0, len(preorder))


if __name__ == '__main__':
    solution = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    solution.build_tree(preorder, inorder)
