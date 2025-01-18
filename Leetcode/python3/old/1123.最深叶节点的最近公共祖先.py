#
# @lc app=leetcode.cn id=1123 lang=python3
#
# [1123] 最深叶节点的最近公共祖先
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    """
        DFS
    """
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # dfs(root) return (lca, depth)
        def dfs(root: Optional[TreeNode]) -> (Optional[TreeNode], int):
            if root is None:
                return (None, 0)
            left , dl = dfs(root.left)
            right, dr = dfs(root.right)
            if dl > dr:
                return (left, dl + 1)
            if dl < dr:
                return (right, dr + 1)
            return (root, dl + 1) # dl == dr
        ans, _ = dfs(root)
        return ans
# @lc code=end

