#
# @lc app=leetcode.cn id=328 lang=python3
#
# [328] 奇偶链表
#
from en.Python3.mod.preImport import *
# @lc code=start
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

# @lc code=end

