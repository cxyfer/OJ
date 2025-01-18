# @algorithm @lc id=83 lang=python3 
# @title remove-duplicates-from-sorted-list


from en.Python3.mod.preImport import *
# @test([1,1,2])=[1,2]
# @test([1,1,2,3,3])=[1,2,3]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        cur = head
        while cur.next:
            if cur.val == cur.next.val: # Skip the next node
                cur.next = cur.next.next
            else: # Move to the next node
                cur = cur.next
        return head