#
# @lc app=leetcode.cn id=2583 lang=python3
#
# [2583] 二叉树中的第 K 大层和
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
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        hp = [] # min heap, size k
        q = deque([root])
        while q:
            cur = 0
            for _ in range(len(q)):
                node = q.popleft()
                cur += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if len(hp) < k:
                heappush(hp, cur)
            else:
                if cur > hp[0]:
                    heapreplace(hp, cur) # first pop then push
        return hp[0] if len(hp) == k else -1
# @lc code=end
