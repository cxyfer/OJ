# @algorithm @lc id=23 lang=python3 
# @title merge-k-sorted-lists


from en.Python3.mod.preImport import *
# @test([[1,4,5],[1,3,4],[2,6]])=[1,1,2,3,4,4,5,6]
# @test([])=[]
# @test([[]])=[]
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