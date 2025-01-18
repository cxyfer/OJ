# @algorithm @lc id=101 lang=python3 
# @title symmetric-tree


from en.Python3.mod.preImport import *
# @test([1,2,2,3,4,4,3])=true
# @test([1,2,2,null,3,null,3])=false
# @test([2,3,3,4,5,null,4])=false
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSameTree(root.left, root.right)
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            return p == q
        return p.val == q.val and self.isSameTree(p.left, q.right) and self.isSameTree(p.right, q.left)