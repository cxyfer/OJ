#
# @lc app=leetcode id=543 lang=python3
# @lcpr version=30204
#
# [543] Diameter of Binary Tree
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root: TreeNode) -> int:
            nonlocal ans
            if root is None:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            ans = max(ans, left + right)
            return max(left, right) + 1
        dfs(root)
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2]\n
# @lcpr case=end

#

