# @algorithm @lc id=783 lang=python3 
# @title search-in-a-binary-search-tree


from en.Python3.mod.preImport import *
# @test([4,2,7,1,3],2)=[2,1,3]
# @test([4,2,7,1,3],5)=[]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if val == root.val:
            return root
        elif val > root.val:
            return self.searchBST(root.right, val)
        else:
            return self.searchBST(root.left, val)