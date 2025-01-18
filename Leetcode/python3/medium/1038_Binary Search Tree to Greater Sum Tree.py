#
# @lc app=leetcode id=1038 lang=python3
# @lcpr version=30204
#
# [1038] Binary Search Tree to Greater Sum Tree
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    Same to 538. Convert BST to Greater Tree
"""
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        s = 0
        def dfs(node: TreeNode) -> None:
            if node is None:
                return
            nonlocal s
            dfs(node.right)
            s += node.val # sum of all nodes >= node.val
            node.val = s
            dfs(node.left)
        dfs(root)
        return root
# @lc code=end



#
# @lcpr case=start
# [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]\n
# @lcpr case=end

# @lcpr case=start
# [0,null,1]\n
# @lcpr case=end

#

