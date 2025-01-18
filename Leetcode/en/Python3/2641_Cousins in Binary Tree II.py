# @algorithm @lc id=2677 lang=python3 
# @title cousins-in-binary-tree-ii


from en.Python3.mod.preImport import *
# @test([5,4,9,1,10,null,7])=[0,0,0,7,7,null,11]
# @test([3,1,2])=[0,0,0]
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
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        root.val = 0
        q = deque([root])
        while q:
            n = len(q)
            s = 0 # sum of values in "next" level
            for node in q: 
                if node.left:
                    s += node.left.val
                if node.right:
                    s += node.right.val
            for _ in range(n):
                node = q.popleft()
                sub = (node.left.val if node.left else 0) + (node.right.val if node.right else 0) # 扣除自己和兄弟節點的值
                if node.left:
                    node.left.val = s - sub
                    q.append(node.left)
                if node.right:
                    node.right.val = s - sub
                    q.append(node.right)
        return root