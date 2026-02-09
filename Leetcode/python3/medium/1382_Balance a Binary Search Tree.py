#
# @lc app=leetcode id=1382 lang=python3
# @lcpr version=30204
#
# [1382] Balance a Binary Search Tree
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Inorder traversal to get the sorted list of values
        nums: List[int] = []
        def inorder(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            inorder(node.left)
            nums.append(node.val)
            inorder(node.right)
        inorder(root)

        # Build the balanced BST from the sorted list
        def build(l: int, r: int) -> Optional[TreeNode]:
            if l > r:
                return None
            mid = (l + r) // 2
            node = TreeNode(nums[mid])
            node.left = build(l, mid - 1)
            node.right = build(mid + 1, r)
            return node
        return build(0, len(nums) - 1)
# @lc code=end



#
# @lcpr case=start
# [1,null,2,null,3,null,4,null,null]\n
# @lcpr case=end

# @lcpr case=start
# [2,1,3]\n
# @lcpr case=end

#

