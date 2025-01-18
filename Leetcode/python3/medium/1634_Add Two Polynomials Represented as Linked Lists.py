#
# @lc app=leetcode id=1634 lang=python3
# @lcpr version=30204
#
# [1634] Add Two Polynomials Represented as Linked Lists
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
# Definition for polynomial singly-linked list.
class PolyNode:
    def __init__(self, x=0, y=0, next=None):
        self.coefficient = x
        self.power = y
        self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        head = PolyNode()
        cur = head
        while poly1 and poly2:
            if poly1.power > poly2.power:
                cur.next = poly1
                poly1 = poly1.next # type: ignore
                cur = cur.next
            elif poly1.power < poly2.power:
                cur.next = poly2
                poly2 = poly2.next # type: ignore
                cur = cur.next
            else:
                s = poly1.coefficient + poly2.coefficient
                if s != 0:
                    cur.next = PolyNode(s, poly1.power)
                    cur = cur.next
                poly1 = poly1.next # type: ignore
                poly2 = poly2.next # type: ignore
        cur.next = poly1 if poly1 is not None else poly2 # type: ignore
        return head.next
# @lc code=end



#
# @lcpr case=start
# [[1,1]]\n[[1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[2,2],[4,1],[3,0]]\n[[3,2],[-4,1],[-1,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,2]]\n[[-1,2]]\n
# @lcpr case=end

#

