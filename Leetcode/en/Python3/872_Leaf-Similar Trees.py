# @algorithm @lc id=904 lang=python3 
# @title leaf-similar-trees


from en.Python3.mod.preImport import *
# @test([3,5,1,6,2,9,8,null,null,7,4],[3,5,1,6,7,4,2,null,null,null,null,null,null,9,8])=true
# @test([1,2,3],[1,3,2])=false
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        """
            1. DFS
        """
        def dfs(node, result):
            if not node:
                return
            if not node.left and not node.right:
                result.append(node.val)
            else:
                dfs(node.left, result)
                dfs(node.right, result)
        res1, res2 = [], []
        dfs(root1, res1)
        dfs(root2, res2)
        return res1 == res2