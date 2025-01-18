# @algorithm @lc id=925 lang=python3 
# @title construct-binary-tree-from-preorder-and-postorder-traversal


from en.Python3.mod.preImport import *
# @test([1,2,4,5,3,6,7],[4,5,2,6,7,3,1])=[1,2,3,4,5,6,7]
# @test([1],[1])=[1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        n = len(postorder)
        if n == 0:
            return None
        root = TreeNode(preorder[0])
        if n == 1:
            return root
        idx = postorder.index(preorder[1]) # let preorder[1] be the root of left subtree, then find the index of preorder[1] in postorder
        root.left = self.constructFromPrePost(preorder[1:idx+2], postorder[:idx+1]) # size of left subtree is idx+1
        root.right = self.constructFromPrePost(preorder[idx+2:], postorder[idx+1:n-1])
        return root