#
# @lc app=leetcode.cn id=2487 lang=python3
#
# [2487] 从链表中移除节点
#
from preImport import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        node = self.removeNodes(head.next) # 剩下裡面最大的
        if node.val > head.val: # 刪除 head
            return node
        head.next = node # 不刪除 head
        return head
# @lc code=end

