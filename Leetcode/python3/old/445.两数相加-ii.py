#
# @lc app=leetcode.cn id=445 lang=python3
#
# [445] 两数相加 II
#
from mod.preImport import *
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        r1 = self.reverseList(l1)
        r2 = self.reverseList(l2)
        carry, sum = 0, 0
        dummy = ListNode()
        p, p1, p2 = dummy, r1, r2
        while p1 or p2:
            sum = carry
            if p1:
                sum += p1.val
                p1 = p1.next
            if p2:
                sum += p2.val
                p2 = p2.next
            carry = sum // 10
            p.next = ListNode(sum%10)
            p = p.next
        if carry:
            p.next = ListNode(carry)
        ans = self.reverseList(dummy.next)
        return ans
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Recursive
        if not head or not head.next:
            return head
        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return last
# @lc code=end

if __name__ == '__main__':
    sol = Solution()
    # print(sol.addTwoNumbers(ListNode(7,ListNode(2,ListNode(4,ListNode(3)))), ListNode(5,ListNode(6,ListNode(4))))) # [7,8,0,7]
    # print(sol.addTwoNumbers(ListNode(2,ListNode(4,ListNode(3))), ListNode(5,ListNode(6,ListNode(4))))) # [8,0,7]
    print(sol.addTwoNumbers(ListNode(0), ListNode(0))) # [0]
    print(sol.addTwoNumbers(ListNode(5), ListNode(5))) # [0]
