# @algorithm @lc id=543 lang=python3 
# @title diameter-of-binary-tree


from en.Python3.mod.preImport import *
# @test([1,2,3,4,5])=3
# @test([1,2])=1
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
            if not root:return 0
            left = dfs(root.left)
            right = dfs(root.right)
            ans = max(ans, left+right)
            return max(left, right) + 1
        dfs(root)
        return ans