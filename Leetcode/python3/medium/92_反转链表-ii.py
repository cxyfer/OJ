#
# @lc app=leetcode.cn id=92 lang=python3
#
# [92] 反转链表 II
#
from preImport import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
    1. Recursive
"""
class Solution1:
    successor = None
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # base case
        if left == 1: 
            return self.reverseN(head, right)
        head.next = self.reverseBetween(head.next, left - 1, right - 1) # 相對左移一位
        return head
    def reverseN(self, head: ListNode, n: int) -> ListNode:
        # base case
        if n == 1:
            self.successor = head.next # Recode the (n+1)-th node
            return head
        # Reverse the first n-1 nodes
        last = self.reverseN(head.next, n - 1) 
        head.next.next = head
        # Connect the last node (head node after reversed) with the (n+1)-th node
        head.next = self.successor
        return last 
"""
    2. Save previos node
    Advanced version of 206. Reverse Linked List
"""
class Solution2:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        part1 = dummy
        for _ in range(left-1):
            part1 = part1.next

        pre = None
        cur = part1.next
        for _ in range(right-left+1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        part1.next.next = cur
        part1.next = pre
        return dummy.next

class Solution(Solution2):
    ...
# @lc code=end

