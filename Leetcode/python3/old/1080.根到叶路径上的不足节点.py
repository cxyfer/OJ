#
# @lc app=leetcode.cn id=1080 lang=python3
#
# [1080] 根到叶路径上的不足节点
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
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(root: TreeNode, sum: int) -> TreeNode:
            if not root: return None
            sum += root.val
            if not root.left and not root.right: # leaf
                return root if sum >= limit else None
            root.left = dfs(root.left, sum)
            root.right = dfs(root.right, sum)
            return root if root.left or root.right else None
        return dfs(root, 0)
# @lc code=end

