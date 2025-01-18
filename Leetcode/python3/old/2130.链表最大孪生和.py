#
# @lc app=leetcode.cn id=2130 lang=python3
#
# [2130] 链表最大孪生和
#
from en.Python3.mod.preImport import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Use two pointers to find the middle node
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Reverse the second half of the linked list
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        # Find the maximum twin sum
        ans = 0
        p1, p2 = head, prev
        while p1 != slow:
            ans = max(ans, p1.val + p2.val)
            p1, p2 = p1.next, p2.next
        return ans
# @lc code=end

