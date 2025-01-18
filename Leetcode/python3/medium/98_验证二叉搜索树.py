#
# @lc app=leetcode.cn id=98 lang=python3
#
# [98] 验证二叉搜索树
#
from preImport import *
# @lc code=start
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: TreeNode, left, right) -> bool:
            if not root: return True
            if not left < root.val < right: return False
            return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)
        return dfs(root, float('-inf'), float('inf'))
# @lc code=end

