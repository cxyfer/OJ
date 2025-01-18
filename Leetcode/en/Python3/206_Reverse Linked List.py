# @algorithm @lc id=206 lang=python3 
# @title reverse-linked-list


from en.Python3.mod.preImport import *
# @test([1,2,3,4,5])=[5,4,3,2,1]
# @test([1,2])=[2,1]
# @test([])=[]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # return self.solveByRecursion(head)
        return self.solveByPreviousNode(head)
    """
        1. Recursive
    """
    def solveByRecursion(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        last = self.reverseList(head.next) 
        head.next.next = head
        head.next = None
        return last
    """
        2. Use previos node
    """
    def solveByPreviousNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre