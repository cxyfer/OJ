#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
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
        Inorder traversal of a BST gives a sorted array.
    """
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # return self.solve1(root)
        return self.solve2(root)
    """
        1. Inorder traversal of a BST gives a sorted array.
        Build the sorted array and find the minimum difference.
    """
    def solve1(self, root: Optional[TreeNode]) -> int:
        def inorder(node):
            if not node:
                return []
            return inorder(node.left) + [node.val] + inorder(node.right)

        arr = inorder(root)
        ans = float('inf')
        for i in range(1, len(arr)):
            ans = min(ans, arr[i] - arr[i-1])
        return ans
    """
        2. Calculate the minimum difference during the inorder traversal.
    """
    def solve2(self, root: TreeNode) -> int:
        ans = float('inf')
        pre = float('-inf')
        
        def dfs(root):
            nonlocal ans, pre
            if not root:
                return 
            dfs(root.left)
            ans = min(ans, root.val - pre)
            pre = root.val
            dfs(root.right)
            
        dfs(root)
        return ans
# @lc code=end
