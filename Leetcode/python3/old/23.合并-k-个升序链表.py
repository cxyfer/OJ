#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并 K 个升序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

# Define the __lt__ and __le__ method for ListNode class
ListNode.__lt__ = lambda self, other: self.val < other.val
ListNode.__le__ = lambda self, other: self.val <= other.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Maintain a heap to store the smallest node of each list
        dummy = ListNode(-1)
        p = dummy
        heap = []
        for node in lists:
            if node:
                heapq.heappush(heap, (node.val, node))
        while heap:
            val, node = heapq.heappop(heap) # pop the smallest node
            p.next = node
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
            p = p.next
        return dummy.next
# @lc code=end

