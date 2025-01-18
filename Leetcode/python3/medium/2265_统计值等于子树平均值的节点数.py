#
# @lc app=leetcode.cn id=2265 lang=python3
#
# [2265] 统计值等于子树平均值的节点数
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
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root: int) -> [int, int]:
            nonlocal ans
            if not root:
                return 0, 0 # sum, cnt
            ls, lc = dfs(root.left)
            rs, rc = dfs(root.right)
            s = ls + rs + root.val # 子樹的和
            c = lc + rc + 1 # 子樹的節點數
            if s // c == root.val:
                ans += 1
            return s, c
        dfs(root)
        return ans
# @lc code=end

