# @algorithm @lc id=908 lang=python3 
# @title middle-of-the-linked-list


from en.Python3.mod.preImport import *
# @test([1,2,3,4,5])=[3,4,5]
# @test([1,2,3,4,5,6])=[4,5,6]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Fast and slow pointers
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        