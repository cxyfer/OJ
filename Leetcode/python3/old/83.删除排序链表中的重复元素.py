#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # The list is guaranteed to be sorted in ascending order.
        # Check if the next node is the same as the cur node.
        if head == None:
            return head
        cur = head
        while cur.next != None:
            if cur.val == cur.next.val: # delete the next node
                cur.next = cur.next.next
            else: # Move to the next node
                cur = cur.next
        return head
# @lc code=end

