# @algorithm @lc id=1116 lang=python3 
# @title maximum-level-sum-of-a-binary-tree


from en.Python3.mod.preImport import *
# @test([1,7,0,7,-8,null,null])=2
# @test([989,null,10250,98693,-89388,null,null,null,-32127])=2
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
        1. BFS
    """
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        ans = defaultdict(int)
        q = deque([(root, 1)])
        while q:
            node, depth = q.popleft()
            if node:
                ans[depth] += node.val
                q.append((node.left, depth + 1))
                q.append((node.right, depth + 1))
        return max(ans, key=ans.get)