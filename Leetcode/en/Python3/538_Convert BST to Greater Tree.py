# @algorithm @lc id=538 lang=python3 
# @title convert-bst-to-greater-tree


from en.Python3.mod.preImport import *
# @test([4,1,6,0,2,5,7,null,null,null,3,null,null,null,8])=[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]
# @test([0,null,1])=[1,null,1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
        Same to 1038. Binary Search Tree to Greater Sum Tree
    """
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s = 0
        def dfs(node: TreeNode):
            nonlocal s
            if not node:
                return
            dfs(node.right)
            node.val += s
            s = node.val
            dfs(node.left)
        dfs(root)
        return root   
        