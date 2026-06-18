#
# @lc app=leetcode id=1302 lang=python3
#
# [1302] Deepest Leaves Sum
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
class Solution1:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        max_depth = max_depth_sum = 0

        def dfs(node: TreeNode, depth: int) -> None:
            nonlocal max_depth, max_depth_sum
            if depth > max_depth:
                max_depth = depth
                max_depth_sum = node.val
            elif depth == max_depth:
                max_depth_sum += node.val
            if node.left is not None:
                dfs(node.left, depth + 1)
            if node.right is not None:
                dfs(node.right, depth + 1)

        dfs(root, 0)

        return max_depth_sum

class Solution2:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        while q:
            max_depth_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                max_depth_sum += node.val
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
        return max_depth_sum


Solution = Solution1
# Solution = Solution2
# @lc code=end

