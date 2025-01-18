#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
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
    """
        Same to 1038. Binary Search Tree to Greater Sum Tree
    """
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s = 0
        def dfs(node: TreeNode):
            nonlocal s
            if not node:
                return
            dfs(node.right)
            node.val += s
            s = node.val
            dfs(node.left)
        dfs(root)
        return root   
# @lc code=end

