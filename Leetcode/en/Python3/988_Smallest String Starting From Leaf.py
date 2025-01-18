# @algorithm @lc id=1030 lang=python3 
# @title smallest-string-starting-from-leaf


from en.Python3.mod.preImport import *
# @test([0,1,2,3,4,3,4])="dba"
# @test([25,1,3,1,3,0,2])="adz"
# @test([2,2,1,null,1,0,null,0])="abc"
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        ans = '~'
        path = []
        def dfs(node):
            nonlocal ans
            if not node:
                return
            path.append(chr(node.val + ord('a')))
            if not node.left and not node.right:
                ans = min(ans, ''.join(reversed(path)))
            dfs(node.left)
            dfs(node.right)
            path.pop()
        dfs(root)
        return ans