# @algorithm @lc id=1157 lang=python3 
# @title insufficient-nodes-in-root-to-leaf-paths


from en.Python3.mod.preImport import *
# @test([1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14],1)=[1,2,3,4,null,null,7,8,9,null,14]
# @test([5,4,8,11,null,17,4,7,1,null,null,5,3],22)=[5,4,8,11,null,17,4,7,null,null,null,5]
# @test([1,2,-3,-5,null,4,null],-1)=[1,null,-3,4]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(root: TreeNode, sum: int) -> TreeNode:
            if not root: return None
            sum += root.val
            if not root.left and not root.right: # leaf
                return root if sum >= limit else None
            root.left = dfs(root.left, sum)
            root.right = dfs(root.right, sum)
            return root if root.left or root.right else None
        return dfs(root, 0)