#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
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
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
            1. DFS
        """
        # def dfs(node):
        #     if not node:
        #         return 0
        #     return max(dfs(node.left), dfs(node.right)) + 1
        # return dfs(root)

        """
            2. BFS
        """
        if not root:
            return 0
        q = deque([root])
        ans = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans += 1
        return ans
# @lc code=end

