#
# @lc app=leetcode id=2471 lang=python3
# @lcpr version=30204
#
# [2471] Minimum Number of Operations to Sort a Binary Tree by Level
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
置換環

Similar question:
- Luogu P8637 交换瓶子
- CF2033E - Sakurako Kosuke and the Permutation
"""
# @lc code=start
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        ans = 0 
        q = deque([root])
        while q:
            n = len(q)
            cur = []
            for _ in range(n):
                node = q.popleft()
                cur.append(node.val)
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

            # 置換環
            A = sorted(range(n), key=lambda i: cur[i])  # 離散化
            ans += n
            vis = [False] * n
            for x in A:
                if vis[x]: continue
                while not vis[x]:
                    vis[x] = True
                    x = A[x]
                # 每個環能減少一次操作
                ans -= 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [1,4,3,7,6,8,5,null,null,null,null,9,null,10]\n
# @lcpr case=end

# @lcpr case=start
# [1,3,2,7,6,5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5,6]\n
# @lcpr case=end

#

