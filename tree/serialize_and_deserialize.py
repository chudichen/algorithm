# Definition for a binary tree node.
import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def helper(root):
            if root:
                arr.append(str(root.val))
                helper(root.left)
                helper(root.right)
            else:
                arr.append("#")

        arr = []
        helper(root)
        return " ".join(arr)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def callHelper(x):
            if not x:
                return
            y = x.popleft()
            if y == "#":
                return
            root = TreeNode(int(y))
            root.left = callHelper(x)
            root.right = callHelper(x)
            return root

        data = data.split()
        x = collections.deque()
        i = 0
        for i in data:
            x.append(i)
        return callHelper(x)


if __name__ == '__main__':
    arr = []
    arr += [0]
