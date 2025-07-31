#
# @lc app=leetcode id=652 lang=python3
#
# [652] Find Duplicate Subtrees
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        mp = defaultdict(TreeNode)
        cnt = defaultdict(int)
        def dfs(node: Optional[TreeNode]) -> str:
            if not node:
                return ""
            expr = f"{node.val}({dfs(node.left)})({dfs(node.right)})"
            mp[expr] = node
            cnt[expr] += 1
            return expr
        dfs(root)
        return [mp[k] for k, v in cnt.items() if v > 1]
# @lc code=end

