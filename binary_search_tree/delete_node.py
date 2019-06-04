"""
删除二分搜索树节点

https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/141/basic-operations-in-a-bst/1006
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return root
        if root.val == key:
            if not root.left and not root.right: return None
            if not root.left: return root.right
            if not root.right: return root.left
            left = root.left
            right = root.right
            p = right
            while p.left: p = p.left
            p.left = left
            return right
        if key > root.val: root.right = self.deleteNode(root.right, key)
        else: root.left = self.deleteNode(root.left, key)
        return root


if __name__ == '__main__':
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    Solution().deleteNode(root, 3)
