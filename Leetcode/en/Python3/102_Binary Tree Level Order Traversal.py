# @algorithm @lc id=102 lang=python3 
# @title binary-tree-level-order-traversal


from en.Python3.mod.preImport import *
# @test([3,9,20,null,null,15,7])=[[3],[9,20],[15,7]]
# @test([1])=[[1]]
# @test([])=[]
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
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root: return ans
        q = deque([root])
        while q:
            cur = []
            for _ in range(len(q)):
                node = q.popleft()
                cur.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            ans.append(cur)
        return ans