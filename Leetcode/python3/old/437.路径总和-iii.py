#
# @lc app=leetcode.cn id=437 lang=python3
#
# [437] 路径总和 III
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
        DFS，同時mantain一個紀錄不同長度的sum的sumList
    """
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, sumList):
            if not node:
                return 0
            sumList = [num + node.val for num in sumList] + [node.val]
            count = sum([1 for num in sumList if num == targetSum])
            return count + dfs(node.left, sumList) + dfs(node.right, sumList)
        ans = dfs(root, [])
        return ans
# @lc code=end

