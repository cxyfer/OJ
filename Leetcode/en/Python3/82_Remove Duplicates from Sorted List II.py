# @algorithm @lc id=82 lang=python3 
# @title remove-duplicates-from-sorted-list-ii


from en.Python3.mod.preImport import *
# @test([1,2,3,3,4,4,5])=[1,2,5]
# @test([1,1,1,2,3])=[2,3]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(0, head)
        cur = dummy
        while cur.next and cur.next.next:
            if cur.next.val == cur.next.next.val:
                nxt = cur.next.next
                while nxt and nxt.val == cur.next.val:
                    nxt = nxt.next
                cur.next = nxt
            else:
                cur = cur.next
        return dummy.next