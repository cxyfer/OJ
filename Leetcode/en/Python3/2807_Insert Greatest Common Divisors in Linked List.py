# @algorithm @lc id=2903 lang=python3 
# @title insert-greatest-common-divisors-in-linked-list


from en.Python3.mod.preImport import *
# @test([18,6,10,3])=[18,6,6,2,10,1,3]
# @test([7])=[7]
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur.next:
            cur.next = ListNode(math.gcd(cur.val, cur.next.val), cur.next)
            cur = cur.next.next
        return head
        