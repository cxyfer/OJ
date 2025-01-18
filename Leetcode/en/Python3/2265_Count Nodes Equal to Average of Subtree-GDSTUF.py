# @algorithm @lc id=2347 lang=python3 
# @title count-nodes-equal-to-average-of-subtree


from en.Python3.mod.preImport import *
# @test([4,8,5,0,1,null,6])=5
# @test([1])=1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root):
            nonlocal ans
            if not root:
                return 0, 0 # sum, cnt
            ls, lc = dfs(root.left)
            rs, rc = dfs(root.right)
            s = ls + rs + root.val
            c = lc + rc + 1
            if s // c == root.val:
                ans += 1
            return s, c
        dfs(root)
        return ans