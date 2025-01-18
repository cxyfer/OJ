# @algorithm @lc id=21 lang=python3 
# @title merge-two-sorted-lists


from en.Python3.mod.preImport import *
# @test([1,2,4],[1,3,4])=[1,1,2,3,4,4]
# @test([],[])=[]
# @test([],[0])=[0]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        cur = head
        p1 = list1
        p2 = list2
        while p1 and p2:
            if p1.val < p2.val:
                cur.next = p1
                p1 = p1.next
            else:
                cur.next = p2
                p2 = p2.next
            cur = cur.next
        if p1:
            cur.next = p1
        if p2:
            cur.next = p2
        return head.next