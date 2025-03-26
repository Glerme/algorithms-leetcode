# 104. Maximum Depth of Binary Tree

# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Input: root = [1,null,2]
# Output: 2

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        if root.val is not None:
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)

        return max(left, right) + 1
