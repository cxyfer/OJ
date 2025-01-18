# @algorithm @lc id=111 lang=python3 
# @title minimum-depth-of-binary-tree


from en.Python3.mod.preImport import *
# @test([3,9,20,null,null,15,7])=2
# @test([2,null,3,null,4,null,5,null,6])=5
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        