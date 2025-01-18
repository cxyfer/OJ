# @algorithm @lc id=975 lang=python3 
# @title range-sum-of-bst


from en.Python3.mod.preImport import *
# @test([10,5,15,3,7,null,18],7,15)=32
# @test([10,5,15,3,7,13,18,1,null,6],6,10)=23
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(root):
            if not root:
                return 0
            if root.val < low:
                return dfs(root.right)
            if root.val > high:
                return dfs(root.left)
            return root.val + dfs(root.left) + dfs(root.right)
        return dfs(root)