#
# @lc app=leetcode.cn id=237 lang=python3
#
# [237] 删除链表中的节点
#
from preImport import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
        由於不能定位到上一個節點，那直接跟下一個節點交換值，然後刪除下一個節點即可
    """
    def deleteNode(self, node):
        node.val = node.next.val # 將當前節點的值和下一個節點的值交換
        node.next = node.next.next # 刪除下一個節點
# @lc code=end

