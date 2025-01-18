# @algorithm @lc id=1092 lang=python3 
# @title maximum-difference-between-node-and-ancestor


from en.Python3.mod.preImport import *
# @test([8,3,10,1,6,null,14,null,null,4,7,13])=7
# @test([1,null,2,null,0,3])=3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], maxVal: int, minVal: int) -> int:
            if not root:
                return maxVal - minVal
            maxVal = max(maxVal, root.val)
            minVal = min(minVal, root.val)
            left = dfs(root.left, maxVal, minVal)
            right = dfs(root.right, maxVal, minVal)
            return max(left, right)
        return dfs(root, root.val, root.val)