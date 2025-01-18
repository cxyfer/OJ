# @algorithm @lc id=513 lang=python3 
# @title find-bottom-left-tree-value


from en.Python3.mod.preImport import *
# @test([2,1,3])=1
# @test([1,2,3,4,null,5,6,null,null,7])=7
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # return self.solve1(root)
        return self.solve2(root)
    def solve1(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        while q:
            cur = []
            for _ in range(len(q)):
                node = q.popleft()
                cur.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return cur[0]
    def solve2(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        while q:
            node = q.popleft()
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return node.val