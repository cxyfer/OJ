# @algorithm @lc id=1498 lang=python3 
# @title find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree


from en.Python3.mod.preImport import *
# @test([7,4,3,null,null,6,19],3)=3
# @test([7],7)=7
# @test([8,null,6,null,5,null,4,null,3,null,2,null,1],4)=4
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        if not original: return None
        if original == target: return cloned
        left = self.getTargetCopy(original.left, cloned.left, target)
        if left: return left
        right = self.getTargetCopy(original.right, cloned.right, target)
        return right