#
# @lc app=leetcode.cn id=872 lang=python3
#
# [872] 叶子相似的树
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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
            1. DFS
        """
        def dfs(node, result):
            if not node:
                return
            if not node.left and not node.right:
                result.append(node.val)
            else:
                dfs(node.left, result)
                dfs(node.right, result)
        res1, res2 = [], []
        dfs(root1, res1)
        dfs(root2, res2)
        return res1 == res2
# @lc code=end

