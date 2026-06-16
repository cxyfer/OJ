#
# @lc app=leetcode id=2095 lang=python3
#
# [2095] Delete the Middle Node of a Linked List
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Fast and Slow Pointer
Advanced of 876. Middle of the Linked List
"""
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, slow, fast = dummy, head, head
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = slow.next
        del slow
        return dummy.next
# @lc code=end

