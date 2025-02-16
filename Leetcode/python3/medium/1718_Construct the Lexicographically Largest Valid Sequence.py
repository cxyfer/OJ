#
# @lc app=leetcode id=1718 lang=python3
# @lcpr version=30204
#
# [1718] Construct the Lexicographically Largest Valid Sequence
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        m = 2 * n - 1
        ans = [-1] * m
        vis = [False] * (n + 1)
        def dfs(i: int) -> bool:
            if i == m:
                return True
            if ans[i] != -1:
                return dfs(i + 1)
            for x in range(n, 0, -1):
                if vis[x]: continue
                if x == 1:
                    ans[i] = 1
                    vis[1] = True
                    if dfs(i + 1):
                        return True
                    ans[i] = -1
                    vis[1] = False
                else:
                    if i + x < m and ans[i + x] == -1:
                        ans[i] = ans[i + x] = x
                        vis[x] = True
                        if dfs(i + 1):
                            return True
                        ans[i] = ans[i + x] = -1
                        vis[x] = False
            return False
        dfs(0)
        return ans
# @lc code=end

sol = Solution()
print(sol.constructDistancedSequence(4))  # [4,2,3,2,4,3,1]

#
# @lcpr case=start
# 3\n
# @lcpr case=end

# @lcpr case=start
# 5\n
# @lcpr case=end

#

