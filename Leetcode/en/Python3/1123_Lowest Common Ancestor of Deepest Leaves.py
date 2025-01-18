# @algorithm @lc id=1218 lang=python3 
# @title lowest-common-ancestor-of-deepest-leaves


from en.Python3.mod.preImport import *
# @test([3,5,1,6,2,0,8,null,null,7,4])=[2,7,4]
# @test([1])=[1]
# @test([0,1,3,null,2])=[2]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
        DFS
    """
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # dfs(root) return (lca, depth)
        def dfs(root: Optional[TreeNode]) -> (Optional[TreeNode], int):
            if root is None:
                return (None, 0)
            left , dl = dfs(root.left)
            right, dr = dfs(root.right)
            if dl > dr:
                return (left, dl + 1)
            if dl < dr:
                return (right, dr + 1)
            return (root, dl + 1) # dl == dr
        ans, _ = dfs(root)
        return ans