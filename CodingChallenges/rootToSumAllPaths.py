# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0 
        stack, res = [(root, root.val)] , 0
        while stack:
            node, value = stack.pop()
            if node:
                if not node.right and not node.left:
                    res += value
                if node.left:
                    stack.append((node.left, value*10+node.left.val))
                if node.right:
                    stack.append((node.right, value*10 + node.right.val))
        return res