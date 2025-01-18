# @algorithm @lc id=2216 lang=python3 
# @title delete-the-middle-node-of-a-linked-list


from en.Python3.mod.preImport import *
# @test([1,3,4,7,1,2,6])=[1,3,4,1,2,6]
# @test([1,2,3,4])=[1,2,4]
# @test([2,1])=[2]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
        Fast and Slow Pointer
        Advanced of 876. Middle of the Linked List
    """
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre, slow, fast = dummy, head, head
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = slow.next
        return dummy.next