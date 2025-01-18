#
# @lc app=leetcode id=2458 lang=python3
# @lcpr version=30204
#
# [2458] Height of Binary Tree After Subtree Removal Queries
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
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        height = defaultdict(int)
        def dfs_height(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            height[node] = max(dfs_height(node.left), dfs_height(node.right)) + 1
            return height[node]
        dfs_height(root)

        res = [0] * (len(height) + 1)
        def dfs(node: Optional[TreeNode], depth: int, rest_h: int) -> None:
            if node is None:
                return
            res[node.val] = rest_h
            dfs(node.left, depth + 1, max(rest_h, depth + height[node.right]))
            dfs(node.right, depth + 1, max(rest_h, depth + height[node.left]))
        dfs(root, 0, 0)

        return [res[q] for q in queries]
# @lc code=end



#
# @lcpr case=start
# [1,3,4,2,null,6,5,null,null,null,null,null,7]\n[4]\n
# @lcpr case=end

# @lcpr case=start
# [5,8,9,2,1,3,7,4,6]\n[3,2,4,8]\n
# @lcpr case=end

#

