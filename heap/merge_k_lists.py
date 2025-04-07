# 23. Merge k Sorted Lists
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.


# Definition for singly-linked list.
import heapq
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        def push_node(heap, node):
            if node:
                heapq.heappush(heap, (node.val, id(node), node))

        for node in lists:
            push_node(heap, node)

        dummy = ListNode()
        current = dummy

        while heap:
            _, _, node = heapq.heappop(heap)
            current.next = node
            current = current.next

            if node.next:
                push_node(heap, node.next)

        return dummy.next
