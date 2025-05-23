# 133. Clone Graph


from collections import deque
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        q = deque([node])

        clones = {}
        clones[node.val] = Node(node.val, [])

        while q:
            current = q.popleft()
            current_clone = clones[current.val]

            for n in current.neighbors:
                if n.val not in clones:
                    clones[n.val] = Node(n.val, [])
                    q.append(n)

                current_clone.neighbors.append(clones[n.val])

        return clones[node.val]
