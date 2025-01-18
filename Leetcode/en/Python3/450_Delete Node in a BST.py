# @algorithm @lc id=450 lang=python3 
# @title delete-node-in-a-bst


from en.Python3.mod.preImport import *
# @test([5,3,6,2,4,null,7],3)=[5,4,6,2,null,null,7]
# @test([5,3,6,2,4,null,7],0)=[5,3,6,2,4,null,7]
# @test([],0)=[]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == key:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            if root.left and root.right: # find the min node in right subtree
                minNode = root.right
                while minNode.left:
                    minNode = minNode.left
                root.val = minNode.val
                root.right = self.deleteNode(root.right, minNode.val)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        return root