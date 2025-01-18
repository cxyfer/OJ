# @algorithm @lc id=144 lang=python3 
# @title binary-tree-preorder-traversal


from en.Python3.mod.preImport import *
# @test([1,null,2,3])=[1,2,3]
# @test([])=[]
# @test([1])=[1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def preorder(root):
            if not root:
                return []
            return [root.val] + preorder(root.left) + preorder(root.right)
        return preorder(root)