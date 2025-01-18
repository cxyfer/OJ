#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
#
from preImport import *
# @lc code=start
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(root: TreeNode) -> TreeNode:
            if not root:return None
            root.left, root.right = dfs(root.right), dfs(root.left)
            return root
        return dfs(root)
# @lc code=end

