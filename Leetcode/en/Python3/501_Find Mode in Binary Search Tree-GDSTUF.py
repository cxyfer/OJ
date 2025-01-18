# @algorithm @lc id=501 lang=python3 
# @title find-mode-in-binary-search-tree


from en.Python3.mod.preImport import *
# @test([1,null,2,2])=[2]
# @test([0])=[0]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        cnt = Counter()
        def dfs(node):
            if node:
                cnt[node.val] += 1
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        maxCnt = max(cnt.values())
        return [k for k, v in cnt.items() if v == maxCnt]