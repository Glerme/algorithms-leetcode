# 100. Same Tree.

# Input: p = [1,2,3], q = [1,2,3]
# Output = True

# Input: p = [1,2], q = [1,null,2]
# Output = False

# Input: p = [1,2,1], q = [1,1,2]
# Output = False

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while i < len(lst):
        node = queue.pop(0)
        if i < len(lst):
            node.left = TreeNode(lst[i])
            queue.append(node.left)
            i += 1
        if i < len(lst):
            node.right = TreeNode(lst[i])
            queue.append(node.right)
            i += 1
    return root


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p is q

        if p.val != q.val:
            return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


p = list_to_tree([1, 2, 3])
q = list_to_tree([1, 2, 3])

print("Solution: ", Solution().isSameTree(p, q))
