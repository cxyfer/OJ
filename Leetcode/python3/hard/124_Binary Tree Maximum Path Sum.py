#
# @lc app=leetcode id=124 lang=python3
# @lcpr version=30204
#
# [124] Binary Tree Maximum Path Sum
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        def dfs(node):
            if node is None: return 0
            nonlocal ans
            left = max(dfs(node.left), 0)  # 不選負數
            right = max(dfs(node.right), 0)  # 不選負數
            ans = max(ans, node.val + left + right)
            return node.val + max(left, right)  # 到葉子的最長路徑
        dfs(root)
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

# @lcpr case=start
# [-10,9,20,null,null,15,7]\n
# @lcpr case=end

#

