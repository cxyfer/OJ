#
# @lc app=leetcode id=687 lang=python3
# @lcpr version=30204
#
# [687] Longest Univalue Path
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
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            nonlocal ans
            left = dfs(node.left) + 1
            right = dfs(node.right) + 1
            if node.left is None or node.left.val != node.val:
                left = 0
            if node.right is None or node.right.val != node.val:
                right = 0
            ans = max(ans, left + right)
            return max(left, right)
        dfs(root)
        return ans
# @lc code=end



#
# @lcpr case=start
# [5,4,5,1,1,null,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,4,5,4,4,null,5]\n
# @lcpr case=end

#

