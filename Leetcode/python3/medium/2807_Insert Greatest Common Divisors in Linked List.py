#
# @lc app=leetcode id=2807 lang=python3
# @lcpr version=30204
#
# [2807] Insert Greatest Common Divisors in Linked List
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head # 當前節點
        while cur.next is not None: # 由於要在每兩個節點之間插入新的節點，所以需要檢查 cur.next 是否存在
            cur.next = ListNode(math.gcd(cur.val, cur.next.val), cur.next) # 插入新的節點
            cur = cur.next.next # 移動到下一個節點
        return head # 返回頭節點
# @lc code=end



#
# @lcpr case=start
# [18,6,10,3]\n
# @lcpr case=end

# @lcpr case=start
# [7]\n
# @lcpr case=end

#

