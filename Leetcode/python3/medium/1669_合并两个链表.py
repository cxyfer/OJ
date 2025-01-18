#
# @lc app=leetcode.cn id=1669 lang=python3
#
# [1669] 合并两个链表
#
from preImport import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode(0, list1)
        p1 = dummy # p1 指向 list1 的第 a-1 個節點
        for _ in range(a):
            p1 = p1.next
        p2 = p1.next # p2 指向 list1 的第 b+1 個節點
        for _ in range(b-a+1):
            p2 = p2.next
        p1.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = p2
        return dummy.next
# @lc code=end

