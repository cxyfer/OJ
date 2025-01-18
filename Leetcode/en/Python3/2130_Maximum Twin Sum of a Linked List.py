# @algorithm @lc id=2236 lang=python3 
# @title maximum-twin-sum-of-a-linked-list


from en.Python3.mod.preImport import *
# @test([5,4,2,1])=6
# @test([4,2,2,3])=7
# @test([1,100000])=100001
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # Use two pointers to find the middle node
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # Reverse the second half of the linked list
        prev, curr = None, slow
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        # Find the maximum twin sum
        ans = 0
        p1, p2 = head, prev
        while p1 != slow:
            ans = max(ans, p1.val + p2.val)
            p1, p2 = p1.next, p2.next
        return ans