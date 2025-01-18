# @algorithm @lc id=94 lang=python3 
# @title binary-tree-inorder-traversal


from en.Python3.mod.preImport import *
# @test([1,null,2,3])=[1,3,2]
# @test([])=[]
# @test([1])=[1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root):
            if not root:
                return []
            return inorder(root.left) + [root.val] + inorder(root.right)
        return inorder(root)