#
# @lc app=leetcode.cn id=2476 lang=python3
#
# [2476] 二叉搜索树最近节点查询
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
    def closestNodes(self, root: Optional[TreeNode], queries: List[int]) -> List[List[int]]:
        nodes = []
        def inorder(node):
            if not node:
                return []
            inorder(node.left)
            nodes.append(node.val)
            inorder(node.right)
        inorder(root)

        ans = []
        for q in queries:
            idx1 = bisect_left(nodes, q) # Find the first element that is not less than q (>=)
            idx2 = bisect_right(nodes, q) # Find the first element that is greater than q (>)
            if idx1 != idx2: # q is in the tree
                ans.append([q, q])
            else:
                if idx1 == 0:
                    ans.append([-1, nodes[idx1]])
                elif idx1 == len(nodes):
                    ans.append([nodes[idx1-1], -1])
                else:
                    ans.append([nodes[idx1-1], nodes[idx1]])
        return ans
# @lc code=end

