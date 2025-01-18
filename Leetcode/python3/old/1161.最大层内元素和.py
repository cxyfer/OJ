#
# @lc app=leetcode.cn id=1161 lang=python3
#
# [1161] 最大层内元素和
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
    """
        1. BFS
    """
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = defaultdict(int)
        q = deque([(root, 1)])
        while q:
            node, depth = q.popleft()
            if node:
                ans[depth] += node.val
                q.append((node.left, depth + 1))
                q.append((node.right, depth + 1))
        return max(ans, key=ans.get)
# @lc code=end

