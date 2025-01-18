#
# @lc app=leetcode id=3193 lang=python3
# @lcpr version=30204
#
# [3193] Count the Number of Inversions
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    Extension of 629. K Inverse Pairs Array
"""

class Solution1:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 10**9 + 7

        mp = defaultdict(int)
        for end, cnt in requirements:
            mp[end] = cnt

        dp = [[0] * 401 for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            if (i - 1) in mp:
                mn = mx = mp[i - 1]
            else:
                mn, mx = 0, 400
            for j in range(mn, mx + 1):
                for k in range(min(i, j+1)):
                    dp[i][j] += dp[i - 1][j - k]
                    dp[i][j] %= MOD

        return sum(dp[n]) % MOD

# WA
class Solution2:
    def numberOfPermutations(self, n: int, requirements: List[List[int]]) -> int:
        MOD = 10**9 + 7

        mp = defaultdict(int)
        for end, cnt in requirements:
            mp[end] = cnt

        @cache
        def dfs(i, j):
            if j == 0:  # 只有由小到大的排列才能有 0 個 Inversions
                return 1
            if i == 0:
                return 0
            if i in mp and j != mp[i]:
                return 0
            ans = 0
            for k in range(min(i, j+1)):  # 這個數字與前面的數字有 k 個 Inversions
                ans += dfs(i - 1, j - k)
                ans %= MOD
            return ans % MOD

        mx = max(mp.values())

        return sum(dfs(n - 1 , j) for j in range(401)) % MOD
    
# class Solution(Solution1):
class Solution(Solution2):
    pass
# @lc code=end

sol = Solution()
print(sol.numberOfPermutations(3, [[2, 2], [0, 0]]))  # 2
print(sol.numberOfPermutations(3, [[2, 2], [1, 1], [0, 0]]))  # 1
print(sol.numberOfPermutations(2, [[0, 0], [1, 0]]))  # 1
print(sol.numberOfPermutations(3, [[1, 0], [2, 1], [0, 0]]))  # 1


#
# @lcpr case=start
# 3\n[[2,2],[0,0]]\n
# @lcpr case=end

# @lcpr case=start
# 3\n[[2,2],[1,1],[0,0]]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[[0,0],[1,0]]\n
# @lcpr case=end

#

