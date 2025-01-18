# @algorithm @lc id=141 lang=python3 
# @title linked-list-cycle


from en.Python3.mod.preImport import *
# @test([3,2,0,-4],1)=true
# @test([1,2],0)=true
# @test([1],-1)=false
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Fast and slow pointer
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return True
        return False