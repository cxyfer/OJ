#
# @lc app=leetcode id=1530 lang=python3
# @lcpr version=30204
#
# [1530] Number of Good Leaf Nodes Pairs
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
# class Solution:
#     def countPairs(self, root: TreeNode, distance: int) -> int:
#         ans = 0
#         def dfs(node):
#             nonlocal ans
#             if not node:
#                 return []
#             if not node.left and not node.right:
#                 return [1]
#             left = dfs(node.left)
#             right = dfs(node.right)
#             res = []
#             for l in left:
#                 for r in right:
#                     if l + r <= distance:
#                         ans += 1
#             return [x + 1 for x in left + right if x + 1 < distance]
#         dfs(root)
#         return ans
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ans = 0
        def dfs(node: TreeNode) -> List[int]:
            cnt = [0] * (distance + 1)
            if not node.left and not node.right: # leaf node
                cnt[0] = 1
                return cnt
            nonlocal ans
            lcnt = dfs(node.left) if node.left else [0] * (distance + 1)
            rcnt = dfs(node.right) if node.right else [0] * (distance + 1)
            for i in range(distance + 1):
                for j in range(distance + 1 - i - 2):
                    ans += lcnt[i] * rcnt[j]
            for i in range(distance):
                cnt[i + 1] = lcnt[i] + rcnt[i]
            return cnt
        dfs(root)
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,2,3,null,4]\n3\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6,7]\n3\n
# @lcpr case=end

# @lcpr case=start
# [7,1,4,6,null,5,3,null,null,null,null,null,2]\n3\n
# @lcpr case=end

#

