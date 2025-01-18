# @algorithm @lc id=445 lang=python3 
# @title add-two-numbers-ii


from en.Python3.mod.preImport import *
from typing import *
# @test([7,2,4,3],[5,6,4])=[7,8,0,7]
# @test([2,4,3],[5,6,4])=[8,0,7]
# @test([0],[0])=[0]
# @test([0], [0])=[0]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r1 = self.reverseList(l1)
        r2 = self.reverseList(l2)
        carry, sum = 0, 0
        dummy = ListNode()
        p, p1, p2 = dummy, r1, r2
        while p1 or p2:
            sum = carry
            if p1:
                sum += p1.val
                p1 = p1.next
            if p2:
                sum += p2.val
                p2 = p2.next
            carry = sum // 10
            p.next = ListNode(sum%10)
            p = p.next
        if carry:
            p.next = ListNode(carry)
        ans = self.reverseList(dummy.next)
        return ans
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive
        if not head or not head.next:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last