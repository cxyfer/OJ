# @algorithm @lc id=1005 lang=python3 
# @title univalued-binary-tree


from en.Python3.mod.preImport import *
# @test([1,1,1,1,1,null,1])=true
# @test([2,2,2,5,2])=false
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
            
        def dfs(node):
            if not node:
                return True
            if node.val != root.val:
                return False
            return dfs(node.left) and dfs(node.right)
            
        return dfs(root)