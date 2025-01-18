# @algorithm @lc id=145 lang=python3 
# @title binary-tree-postorder-traversal


from en.Python3.mod.preImport import *
# @test([1,null,2,3])=[3,2,1]
# @test([])=[]
# @test([1])=[1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def postorder(root):
            if not root:
                return []
            return postorder(root.left) + postorder(root.right) + [root.val]
        return postorder(root)