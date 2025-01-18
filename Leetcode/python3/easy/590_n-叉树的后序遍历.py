#
# @lc app=leetcode.cn id=590 lang=python3
#
# [590] N 叉树的后序遍历
#
from preImport import *
# @lc code=start
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def dfs(node):
            res = []
            if node is None:
                return res
            res = []
            for child in node.children:
                res += dfs(child)
            res.append(node.val)
            return res
        return dfs(root)
# @lc code=end

