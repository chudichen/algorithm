"""
重建二叉树

根据前序遍历以及中序遍历重建二叉树,前序遍历是中左右，中序遍历左中右。
用前序遍历确定中间的位置，中序遍历确定左右两侧的位置。
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""


# Definition for a binary tree node.
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
    		parent.left(i, split_index)
    		parent.right(split_index + 1, j)
    		return parent
		return buildNode(0, len(preorder))

if __name__ == '__main__':
    solution = Solution()
    solution.build_tree([1], [2])
