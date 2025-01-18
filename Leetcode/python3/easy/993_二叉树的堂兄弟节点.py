#
# @lc app=leetcode.cn id=993 lang=python3
#
# [993] 二叉树的堂兄弟节点
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
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        depth1, depth2 = -1, -1
        parent1, parent2 = None, None
        q = deque([(root, 0, None)])
        while (depth1 == -1 or depth2 == -1):
            node, depth, parent = q.popleft()
            if node.val == x:
                depth1, parent1 = depth, parent
            if node.val == y:
                depth2, parent2 = depth, parent
            if node.left:
                q.append((node.left, depth+1, node))
            if node.right:
                q.append((node.right, depth+1, node))
        return (depth1 == depth2 and parent1 != parent2)
# @lc code=end

