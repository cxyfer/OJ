#
# @lc app=leetcode id=979 lang=python3
# @lcpr version=30202
#
# [979] Distribute Coins in Binary Tree
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
        DFS
        Similar to UVA-10672
    """
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # return self.solve1(root)
        return self.solve2(root)
    def solve1(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root: TreeNode) -> Tuple[int, int]: # (need, have)
            if not root:
                return 0, 0
            nonlocal ans
            p, q = 1, root.val # need, have
            p1, q1 = dfs(root.left)
            p2, q2 = dfs(root.right)
            p += p1 + p2
            q += q1 + q2
            ans += abs(p - q)
            return p, q
        dfs(root)
        return ans
    def solve2(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(root: TreeNode) -> int: # 正數表示多餘的硬幣，負數表示缺少的硬幣
            nonlocal ans
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            ans += abs(left) + abs(right)
            return root.val + left + right - 1
        dfs(root)
        return ans
# @lc code=end



#
# @lcpr case=start
# [3,0,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,3,0]\n
# @lcpr case=end

#

