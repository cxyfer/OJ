# @algorithm @lc id=2 lang=python3 
# @title add-two-numbers


from en.Python3.mod.preImport import *
# @test([2,4,3],[5,6,4])=[7,0,8]
# @test([0],[0])=[0]
# @test([9,9,9,9,9,9,9],[9,9,9,9])=[8,9,9,9,0,0,0,1]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        cur = head
        carry = 0 # Carry
        while (l1 or l2 or carry):
            val = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            carry = val >= 10
            cur.next = ListNode(val % 10)
            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next
        