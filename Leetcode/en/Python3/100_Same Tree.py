# @algorithm @lc id=100 lang=python3 
# @title same-tree


from en.Python3.mod.preImport import *
# @test([1,2,3],[1,2,3])=true
# @test([1,2],[1,null,2])=false
# @test([1,2,1],[1,1,2])=false
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p == q