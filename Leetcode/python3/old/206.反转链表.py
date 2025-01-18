#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
from en.Python3.mod.preImport import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
        1. Recursive
    """
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head or not head.next:
    #         return head
    #     last = self.reverseList(head.next) 
    #     head.next.next = head
    #     head.next = None
    #     return last
    """
        2. Use previos node
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
# @lc code=end

