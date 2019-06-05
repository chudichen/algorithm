"""
寻找最小公共祖先节点

利用递归

https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/142/conclusion/1012/
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root
        left, right = None, None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right


if __name__ == '__main__':
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)
    root.right = TreeNode(8)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    right = TreeNode(4)
    right.left = TreeNode(3)
    right.right = TreeNode(5)
    res = Solution().lowestCommonAncestor(root, TreeNode(0), TreeNode(3))
    print(res)
