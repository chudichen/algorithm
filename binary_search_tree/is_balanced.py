"""


https://leetcode.com/explore/learn/card/introduction-to-data-structure-binary-search-tree/143/appendix-height-balanced-bst/1027/
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def backtracking(root):
            if not root:
                return 1
            left = backtracking(root.left)
            if not left:
                return 0
            right = backtracking(root.right)
            if not right:
                return 0
            return max(left, right)+1 if abs(left - right) <= 1 else 0
        if not root:
            return True
        return True if backtracking(root) else False


if __name__ == '__main__':
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    res = Solution().isBalanced(root)
    assert res is True
