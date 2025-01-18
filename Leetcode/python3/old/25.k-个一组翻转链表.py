#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] K 个一组翻转链表
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
        Advanced version of 92. Reverse Linked List II
    """
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        tmp = head
        while tmp:
            n += 1
            tmp = tmp.next

        dummy = ListNode(next=head)
        p0 = dummy # 上一段的結尾

        while(n >= k):
            n -= k
            pre = None
            cur = p0.next # 上一段的結尾後一個
            for _ in range(k):
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt

            nxt = p0.next 
            p0.next.next = cur # 下一段的開頭
            p0.next = pre # 這一段的開頭(原本的結尾)
            p0 = nxt 
        return dummy.next
# @lc code=end

