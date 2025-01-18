# @algorithm @lc id=124 lang=python3 
# @title binary-tree-maximum-path-sum


from en.Python3.mod.preImport import *
# @test([1,2,3])=6
# @test([-10,9,20,null,null,15,7])=42
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        @cache
        def dfs(node):
            nonlocal ans
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            ans = max(ans, node.val + left + right)
            return node.val + max(left, right)
        dfs(root)
        return ans