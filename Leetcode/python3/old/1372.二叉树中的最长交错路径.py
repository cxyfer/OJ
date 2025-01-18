#
# @lc app=leetcode.cn id=1372 lang=python3
#
# [1372] 二叉树中的最长交错路径
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
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        # l,r 分別代表以當前節點為左/右節點的最長交錯路徑
        def dfs(root: TreeNode, l:int, r:int) -> int:
            if not root: return max(l, r) - 1
            left = dfs(root.left, 0, l+1)
            right = dfs(root.right, r+1, 0)
            return max(left, right)
        return dfs(root, 0, 0)
# @lc code=end

