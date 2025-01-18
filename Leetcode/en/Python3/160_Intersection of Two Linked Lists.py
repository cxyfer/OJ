# @algorithm @lc id=160 lang=python3 
# @title intersection-of-two-linked-lists


from en.Python3.mod.preImport import *
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # https://labuladong.github.io/algo/images/%E9%93%BE%E8%A1%A8%E6%8A%80%E5%B7%A7/6.jpeg
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
        return p1