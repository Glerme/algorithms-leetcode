# 94. Binary Tree Inorder Traversal.

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def in_order(root):
            return in_order(root.left) + [root.val] + in_order(root.right) if root else []
        return in_order(root)
