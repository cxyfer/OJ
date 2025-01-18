#
# @lc app=leetcode.cn id=199 lang=python3
#
# [199] 二叉树的右视图
#
from en.Python3.mod.preImport import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
        1. BFS
    """
    # def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    #     if not root:
    #         return []
    #     q = deque([root])
    #     ans = []
    #     while q:
    #         ans.append(q[-1].val) # 紀錄每層最右邊的節點的值
    #         n = len(q) # 紀錄當前層的節點數量
    #         for _ in range(n): # 將當前層的節點彈出，並將下一層的節點加入
    #             node = q.popleft()
    #             if node.left:
    #                 q.append(node.left)
    #             if node.right:
    #                 q.append(node.right)
    #     return ans
    """
        2. DFS
        依照root => right => left的順序遍歷，並記錄每層第一個遍歷到的節點的值
    """
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = []
        def dfs(node, depth):
            if not node:
                return
            if len(ans) == depth:
                ans.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return ans
# @lc code=end

