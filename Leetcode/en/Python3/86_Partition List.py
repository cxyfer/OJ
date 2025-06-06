# @algorithm @lc id=86 lang=python3 
# @title partition-list


from en.Python3.mod.preImport import *
# @test([1,4,3,2,5,2],3)=[1,2,2,4,3,5]
# @test([2,1],2)=[1,2]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy1 = ListNode(-1)
        dummy2 = ListNode(-1)
        p1 = dummy1
        p2 = dummy2
        p = head
        while p:
            if p.val < x:
                p1.next = p
                p1 = p1.next
            else:
                p2.next = p
                p2 = p2.next
            p = p.next
        p1.next = dummy2.next
        p2.next = None
        return dummy1.next