# @algorithm @lc id=515 lang=python3 
# @title find-largest-value-in-each-tree-row


from en.Python3.mod.preImport import *
# @test([1,3,2,5,3,null,9])=[1,3,9]
# @test([1,2,3])=[1,3]
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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            n = len(q) # number of nodes in this level
            max_val = float('-inf') # max value in this level
            for _ in range(n):
                node = q.popleft()
                max_val = max(max_val, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(max_val)
        return ans