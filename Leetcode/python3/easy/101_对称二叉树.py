#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#
from preImport import *
# @lc code=start
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSameTree(root.left, root.right)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p == q
        return p.val == q.val and self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)
# @lc code=end

