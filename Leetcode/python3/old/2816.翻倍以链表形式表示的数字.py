#
# @lc app=leetcode.cn id=2816 lang=python3
#
# [2816] 翻倍以链表形式表示的数字
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        if head.val >= 5:
            head = ListNode(0, head)
        cur = head
        while cur != None:
            cur.val = cur.val * 2 % 10
            if cur.next and cur.next.val >= 5:
                cur.val += 1
            cur = cur.next
        return head


# @lc code=end

