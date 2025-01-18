#
# @lc app=leetcode id=968 lang=python3
# @lcpr version=30203
#
# [968] Binary Tree Cameras
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
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode) -> List[int]:
            res = [0, 0]
            if not node:
                return res
            left = dfs(node.left)
            right = dfs(node.right)
            res[0] = left[1] + right[1]
            res[1] = min(left) + min(right) + 1
            return res
        return min(dfs(root))
        
# @lc code=end



#
# @lcpr case=start
# [0,0,null,0,0]\n
# @lcpr case=end

# @lcpr case=start
# [0,0,null,0,null,0,null,null,0]\n
# @lcpr case=end

#

