#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root: TreeNode) -> TreeNode:
            if not root: return None
            root.left, root.right = dfs(root.right), dfs(root.left)
            return root
        return dfs(root)
# @lc code=end

