# @algorithm @lc id=1267 lang=python3 
# @title remove-zero-sum-consecutive-nodes-from-linked-list


from en.Python3.mod.preImport import *
# @test([1,2,-3,3,1])=[3,1]
# @test([1,2,3,-3,4])=[1,2,4]
# @test([1,2,3,-3,-2])=[1]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
        Prefix Sum + Hash Table
    """
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(val=0, next=head)
        last = dict() # last[s] = node, the last node with prefix sum s
        s = 0 # prefix sum
        cur = dummy
        while cur: # get the last node with prefix sum s
            s += cur.val
            last[s] = cur
            cur = cur.next
        s, cur = 0, dummy
        while cur: # remove the nodes between last[s] and cur
            s += cur.val
            cur.next = last[s].next
            cur = cur.next
        return dummy.next
