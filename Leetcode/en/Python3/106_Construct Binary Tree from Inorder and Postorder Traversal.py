# @algorithm @lc id=106 lang=python3 
# @title construct-binary-tree-from-inorder-and-postorder-traversal


from en.Python3.mod.preImport import *
# @test([9,3,15,20,7],[9,15,7,20,3])=[3,9,20,null,null,15,7]
# @test([-1],[-1])=[-1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(postorder)
        if n == 0:
            return None
        root = TreeNode(postorder[-1])
        idx = inorder.index(postorder[-1]) # root index in inorder, also the size of left subtree
        root.left = self.buildTree(inorder[:idx], postorder[:idx])
        root.right = self.buildTree(inorder[idx+1:], postorder[idx:n-1])
        return root