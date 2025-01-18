#
# @lc app=leetcode.cn id=1457 lang=python3
#
# [1457] 二叉树中的伪回文路径
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
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        ans = 0
        cnt = Counter()
        def dfs(root):
            if not root:
                return 0
            cnt[root.val] += 1
            if not root.left and not root.right: # leaf
                tmp = 0
                for v in cnt.values():
                    if v % 2 != 0:
                        tmp += 1
                cnt[root.val] -= 1
                return 1 if tmp <= 1 else 0 # 奇數個數最多只能有一個
            ans = dfs(root.left) + dfs(root.right)
            cnt[root.val] -= 1
            return ans
        
        return dfs(root)
# @lc code=end

