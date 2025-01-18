#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#
from en.Python3.mod.preImport import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # def dfs(root: TreeNode) -> int:
        #     if not root: return 0
        #     left = dfs(root.left)
        #     right = dfs(root.right)
        #     return max(left, right) + 1
        # if not root: return True
        # if not root.left and not root.right: return True
        # if abs(dfs(root.left) - dfs(root.right)) > 1: return False
        # return self.isBalanced(root.left) and self.isBalanced(root.right)
        def dfs(root: TreeNode) -> int:
            if not root:
                return 0
            left = dfs(root.left)
            if left == -1:
                return -1
            right = dfs(root.right)
            if right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1
        return dfs(root) != -1
# @lc code=end

