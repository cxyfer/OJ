#
# @lc app=leetcode id=1367 lang=python3
# @lcpr version=30204
#
# [1367] Linked List in Binary Tree
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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        # 從當前位置開始，或從左右子樹開始
        return self.dfs(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
    
    def dfs(self, head, root):
        if not head: # LinkedList 中所有值皆能在 Tree 中找到
            return True
        if not root: # 還沒走完 LinkedList 但 Tree 已經走完
            return False
        if head.val != root.val: # 該位置無法對應
            return False
        # 繼續往下一個位置尋找(左或右)
        return self.dfs(head.next, root.left) or self.dfs(head.next, root.right) 
# @lc code=end



#
# @lcpr case=start
# [4,2,8]\n[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,4,2,6]\n[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]\n
# @lcpr case=end

# @lcpr case=start
# [1,4,2,6,8]\n[1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]\n
# @lcpr case=end

#

