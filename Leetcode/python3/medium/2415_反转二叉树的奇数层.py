#
# @lc app=leetcode.cn id=2415 lang=python3
#
# [2415] 反转二叉树的奇数层
#
from preImport import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = 0
        q = deque([root])
        while q:
            n = len(q)
            if level % 2 == 1:
                for i in range(n // 2):
                    q[i].val, q[-i - 1].val = q[-i - 1].val, q[i].val
            for _ in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return root
# @lc code=end

