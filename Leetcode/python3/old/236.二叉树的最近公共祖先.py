#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
#
from en.Python3.mod.preImport import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
        若 root 是 p, q 的 最近共同祖先，則只可能為以下情況之一：
            1. p 和 q 分別在 root 的 左/右子樹中
            2. p = root，且 q 在 root 的 左/右子樹中
            3. q = root，且 p 在 root 的 左/右子樹中
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        if p == root or q == root: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if not left and not right: # a. p 和 q 都不在 root 的 左/右子樹中
            return None
        elif not right:
            return left
        elif not left: 
            return right
        else: # p 和 q 分別在 root 的 左/右子樹中
            return root

# @lc code=end

