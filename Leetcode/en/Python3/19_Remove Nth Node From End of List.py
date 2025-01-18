# @algorithm @lc id=19 lang=python3 
# @title remove-nth-node-from-end-of-list


from en.Python3.mod.preImport import *
# @test([1,2,3,4,5],2)=[1,2,3,5]
# @test([1],1)=[]
# @test([1,2],1)=[1]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        # Find (k+1)th node from the end
        p1 = dummy
        for i in range(n+1):
            p1 = p1.next
        p2 = dummy
        while p1 != None:
            p2 = p2.next
            p1 = p1.next
        # p2 now point to the (k+1)th node from the end
        p2.next = p2.next.next
        return dummy.next