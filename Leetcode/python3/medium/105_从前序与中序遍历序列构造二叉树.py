#
# @lc app=leetcode.cn id=105 lang=python3
#
# [105] 从前序与中序遍历序列构造二叉树
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
        Recursion
        root is the first element in preorder, and it divides inorder into left and right subtrees.
        let idx be the index of root in inorder, which is also the size of left subtree, then:
        - left subtree: 
            - preorder: preorder[1], preorder[2], ..., preorder[idx]
            - inorder: inorder[0], inorder[1], ..., inorder[idx-1]
        - right subtree:
            - preorder: preorder[idx+1], ..., preorder[n-1]
            - inorder: inorder[idx+1], ..., inorder[n-1]
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        idx = inorder.index(preorder[0]) # root index in inorder, also the size of left subtree
        root.left = self.buildTree(preorder[1:idx+1], inorder[:idx])
        root.right = self.buildTree(preorder[idx+1:], inorder[idx+1:])
        return root
# @lc code=end

