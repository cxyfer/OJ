# @algorithm @lc id=257 lang=python3 
# @title binary-tree-paths


from en.Python3.mod.preImport import *
# @test([1,2,3,null,5])=["1->2->5","1->3"]
# @test([1])=["1"]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        """
            Backtracking
        """
        ans = []
        res = []
        def backtrace(cur) -> None:
            res.append(str(cur.val))
            if not cur.left and not cur.right:
                ans.append('->'.join(res))
            if cur.left:
                backtrace(cur.left)
            if cur.right:
                backtrace(cur.right)
            res.pop()
        backtrace(root)
        return ans