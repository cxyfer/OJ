#
# @lc app=leetcode id=515 lang=python3
# @lcpr version=30204
#
# [515] Find Largest Value in Each Tree Row
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
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        ans = []
        q = deque([root])
        while q:
            mx = -float("inf")
            for _ in range(len(q)):
                node = q.popleft()
                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
                mx = max(mx, node.val)
            ans.append(mx)
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,3,2,5,3,null,9]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#

