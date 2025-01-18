# @algorithm @lc id=98 lang=python3 
# @title validate-binary-search-tree


from en.Python3.mod.preImport import *
# @test([2,1,3])=true
# @test([5,1,4,null,null,3,6])=false
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: TreeNode, left, right) -> bool:
            if not root: return True
            if not left < root.val < right: return False
            return dfs(root.left, left, root.val) and dfs(root.right, root.val, right)
        return dfs(root, float('-inf'), float('inf'))