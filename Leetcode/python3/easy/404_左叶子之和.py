#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, isLeft: bool) -> int:
            if not node:
                return 0
            if not node.left and not node.right and isLeft: # is leaf node and is left node
                return node.val
            return dfs(node.left, True) + dfs(node.right, False)
        return dfs(root, False)
# @lc code=end

