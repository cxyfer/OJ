# @algorithm @lc id=114 lang=python3 
# @title flatten-binary-tree-to-linked-list


from en.Python3.mod.preImport import *
# @test([1,2,5,3,4,null,6])=[1,null,2,null,3,null,4,null,5,null,6]
# @test([])=[]
# @test([0])=[0]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        cur = root
        while cur:
            if cur.left:
                nxt = cur.left
                predecessor = cur.left # predecessor 前驅節點，左子樹的最右節點
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = cur.right # 將前驅節點的右子樹指向當前節點的右子樹
                cur.left = None
                cur.right = nxt
            cur = cur.right