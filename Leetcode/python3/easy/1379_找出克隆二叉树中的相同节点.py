#
# @lc app=leetcode.cn id=1379 lang=python3
#
# [1379] 找出克隆二叉树中的相同节点
#
from preImport import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original: return None
        if original == target: return cloned
        left = self.getTargetCopy(original.left, cloned.left, target)
        if left: return left
        right = self.getTargetCopy(original.right, cloned.right, target)
        return right
# @lc code=end

