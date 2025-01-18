#
# @lc app=leetcode.cn id=1448 lang=python3
#
# [1448] 统计二叉树中好节点的数目
#
from mod.preImport import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS
        def dfs(root: TreeNode, max_val: int) -> int:
            if not root:
                return 0
            max_val = max(max_val, root.val) # update max_val
            # Check if current node is a good node
            return (1 if root.val >= max_val else 0) + dfs(root.left, max_val) + dfs(root.right, max_val)
        return dfs(root, root.val)
# @lc code=end

