#
# @lc app=leetcode.cn id=236 lang=python3
#
# [236] 二叉树的最近公共祖先
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
    """
        若 root 是 p, q 的 最近共同祖先，則只可能為以下情況之一：
            1. p 和 q 分別在 root 的 左/右子樹中
            2. p = root，且 q 在 root 的 左/右子樹中
            3. q = root，且 p 在 root 的 左/右子樹中
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # return self.solve1(root, p, q)
        return self.solve2(root, p, q)
    """
        1. Recursion
    """
    def solve1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        if p == root or q == root: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right: # p 和 q 分別在 root 的 左/右子樹中
            return root
        elif left:
            return left
        elif right:
            return right
        else: # p 和 q 都不在 root 的 左/右子樹中
            return None
    """
        2. Recode the parent of each node
    """
    def solve2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        fa = {root.val: None}
        visited = set()

        def dfs(root: 'TreeNode'):
            if root.left:
                fa[root.left.val] = root
                dfs(root.left)
            if root.right:
                fa[root.right.val] = root
                dfs(root.right)
        dfs(root)

        while p != None:
            visited.add(p.val)
            p = fa[p.val]

        while q != None:
            if q.val in visited:
                return q
            q = fa[q.val]

        return None
# @lc code=end

