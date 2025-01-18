#
# @lc app=leetcode.cn id=2641 lang=python3
#
# [2641] 二叉树的堂兄弟节点 II
#
from preImport import *
# @lc code=start
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
# @lc code=end

