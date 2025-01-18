#
# @lc app=leetcode id=1325 lang=python3
# @lcpr version=30202
#
# [1325] Delete Leaves With a Given Value
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root:
            return None
        root.left = self.removeLeafNodes(root.left, target)
        root.right = self.removeLeafNodes(root.right, target)
        return None if not root.left and not root.right and root.val == target else root
# @lc code=end



#
# @lcpr case=start
# [1,2,3,2,null,2,4]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,3,3,3,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,null,2,null,2]\n2\n
# @lcpr case=end

#

