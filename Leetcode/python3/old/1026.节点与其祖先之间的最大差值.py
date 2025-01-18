#
# @lc app=leetcode.cn id=1026 lang=python3
#
# [1026] 节点与其祖先之间的最大差值
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
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], maxVal: int, minVal: int) -> int:
            if not root:
                return maxVal - minVal
            maxVal = max(maxVal, root.val)
            minVal = min(minVal, root.val)
            left = dfs(root.left, maxVal, minVal)
            right = dfs(root.right, maxVal, minVal)
            return max(left, right)
        return dfs(root, root.val, root.val)
# @lc code=end

