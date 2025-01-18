#
# @lc app=leetcode.cn id=589 lang=python3
#
# [589] N 叉树的前序遍历
#
from preImport import *
# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(node):
            res = []
            if node is None:
                return res
            res = [node.val]
            for child in node.children:
                res += dfs(child)
            return res
        return dfs(root)
# @lc code=end

