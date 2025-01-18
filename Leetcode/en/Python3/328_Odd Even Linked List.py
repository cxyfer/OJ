# @algorithm @lc id=328 lang=python3 
# @title odd-even-linked-list


from en.Python3.mod.preImport import *
# @test([1,2,3,4,5])=[1,3,5,2,4]
# @test([2,1,3,5,6,4,7])=[2,3,6,7,1,5,4]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        p1, p2 = head, head.next
        dummy1, dummy2 = ListNode(0, p1), ListNode(0, p2)
        while p1.next and p2.next:
            p1.next = p2.next
            p1 = p1.next
            p2.next = p1.next
            p2 = p2.next
        p1.next = dummy2.next
        return dummy1.next