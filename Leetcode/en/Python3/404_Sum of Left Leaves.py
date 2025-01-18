# @algorithm @lc id=404 lang=python3 
# @title sum-of-left-leaves


from en.Python3.mod.preImport import *
# @test([3,9,20,null,null,15,7])=24
# @test([1])=0
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, isLeft: bool) -> int:
            if not node:
                return 0
            if not node.left and not node.right and isLeft: # is leaf node and is left node
                return node.val
            return dfs(node.left, True) + dfs(node.right, False)
        return dfs(root, False)