# @algorithm @lc id=1544 lang=python3 
# @title count-good-nodes-in-binary-tree


from en.Python3.mod.preImport import *
# @test([3,1,4,3,null,1,5])=4
# @test([3,3,null,4,2])=3
# @test([1])=1
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # DFS
        def dfs(root: TreeNode, max_val: int) -> int:
            if not root:
                return 0
            max_val = max(max_val, root.val) # update max_val
            # Check if current node is a good node
            return (1 if root.val >= max_val else 0) + dfs(root.left, max_val) + dfs(root.right, max_val)
        return dfs(root, root.val)
        