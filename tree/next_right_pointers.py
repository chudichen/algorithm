"""
计算下一个右边指针

其实就是广度优先遍历

https://leetcode.com/explore/learn/card/data-structure-tree/133/conclusion/994/
"""


# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        stack = [root]
        while stack:
            pre = None
            next_level = []
            while stack:
                cur = stack.pop()
                cur.next = pre
                pre = cur
                if cur.right is None:
                    continue
                next_level.insert(0, cur.right)
                next_level.insert(0, cur.left)
            stack = next_level
        return root

