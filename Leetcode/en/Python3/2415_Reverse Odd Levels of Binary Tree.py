# @algorithm @lc id=2493 lang=python3 
# @title reverse-odd-levels-of-binary-tree


from en.Python3.mod.preImport import *
# @test([2,3,5,8,13,21,34])=[2,5,3,8,13,21,34]
# @test([7,13,11])=[7,11,13]
# @test([0,1,2,0,0,0,0,1,1,1,1,2,2,2,2])=[0,2,1,0,0,0,0,2,2,2,2,1,1,1,1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        level = 0
        q = deque([root])
        while q:
            n = len(q)
            if level % 2 == 1:
                for i in range(n // 2):
                    q[i].val, q[-i - 1].val = q[-i - 1].val, q[i].val
            for _ in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return root