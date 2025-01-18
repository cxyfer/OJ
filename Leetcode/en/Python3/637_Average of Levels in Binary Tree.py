# @algorithm @lc id=637 lang=python3 
# @title average-of-levels-in-binary-tree


from en.Python3.mod.preImport import *
# @test([3,9,20,null,null,15,7])=[3.00000,14.50000,11.00000]
# @test([3,9,20,15,7])=[3.00000,14.50000,11.00000]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
        Level order traversal
    """
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        q = deque([root])
        while q:
            n = len(q)
            s = 0
            for _ in range(n):
                node = q.popleft()
                s += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(s/n)
        return ans