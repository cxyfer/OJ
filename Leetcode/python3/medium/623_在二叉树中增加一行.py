#
# @lc app=leetcode.cn id=623 lang=python3
#
# [623] 在二叉树中增加一行
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
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # return self.solve1(root, val, depth)
        return self.solve2(root, val, depth)
    """
        1. DFS
    """
    def solve1(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:

        def dfs(node: TreeNode, cur: int):
            if not node:
                return
            if cur == depth - 1:
                node.left = TreeNode(val=val, left=node.left)
                node.right = TreeNode(val=val, right=node.right)
            else:
                dfs(node.left, cur + 1)
                dfs(node.right, cur + 1)

        if depth == 1:
            return TreeNode(val=val, left=root)
        dfs(root, 1)
        return root
    """
        2. BFS
    """
    def solve2(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val=val, left=root)
        q = deque([(root, 1)])
        while q:
            node, cur = q.popleft()
            if cur == depth - 1:
                node.left = TreeNode(val=val, left=node.left)
                node.right = TreeNode(val=val, right=node.right)
            else:
                if node.left:
                    q.append((node.left, cur + 1))
                if node.right:
                    q.append((node.right, cur + 1))
        return root
# @lc code=end

