#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Advaced of 141. Linked List Cycle
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Has cycle or not
        # Using fast and slow pointer
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                break
        if not fast or not fast.next:
            return None
        # Find the entry of the cycle
        # https://labuladong.github.io/algo/images/%E5%8F%8C%E6%8C%87%E9%92%88/2.jpeg
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow
# @lc code=end

