# @algorithm @lc id=103 lang=python3 
# @title binary-tree-zigzag-level-order-traversal


from en.Python3.mod.preImport import *
# @test([3,9,20,null,null,15,7])=[[3],[20,9],[15,7]]
# @test([1])=[[1]]
# @test([])=[]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if not root:
            return ans
        lvl = 0 # level
        q = deque([root])
        while q:
            cur = []
            for _ in range(len(q)):
                node = q.popleft()
                cur.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if lvl & 1: # if lvl % 2 != 0
                cur.reverse()
            ans.append(cur)
            lvl += 1
        return ans