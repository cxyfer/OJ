#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        path = []
        def dfs(node, targetSum):
            if node is None:
                return
            path.append(node.val)
            targetSum -= node.val
            if node.left is None and node.right is None and targetSum == 0:
                ans.append(path[:])
            dfs(node.left, targetSum)
            dfs(node.right, targetSum)
            path.pop()
        dfs(root, targetSum)
        return ans
# @lc code=end

