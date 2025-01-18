#
# @lc app=leetcode id=740 lang=python3
# @lcpr version=30201
#
# [740] Delete and Earn
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        Dynamic Programming (DP)
        Similar to 198. House Robber

        1. O(n + mx)
        2. O(n log n)
    """
    def deleteAndEarn(self, nums: List[int]) -> int:
        # return self.solve1a(nums)
        # return self.solve1b(nums)
        return self.solve1c(nums)
        # return self.solve2a(nums)
        # return self.solve2b(nums)
        # return self.solve2c(nums)
    def solve1a(self, nums: List[int]) -> int:
        mx = max(nums)
        cnt = [0] * (mx + 1)
        for x in nums:
            cnt[x] += 1
        @cache
        def dfs(i: int) -> int:
            if i < 0:
                return 0
            return max(dfs(i-1), dfs(i-2) + cnt[i] * i)
        return dfs(mx)
    def solve1b(self, nums: List[int]) -> int:
        mx = max(nums)
        cnt = [0] * (mx + 1)
        for x in nums:
            cnt[x] += 1
        dp = [0] * (mx + 1)
        dp[1] = cnt[1]
        for i in range(2, mx+1):
            dp[i] = max(dp[i-1], dp[i-2] + cnt[i] * i)
        return dp[mx]
    def solve1c(self, nums: List[int]) -> int:
        mx = max(nums)
        cnt = [0] * (mx + 1)
        for x in nums:
            cnt[x] += 1
        f0, f1 = 0, 0
        for x in range(1, mx+1):
            f0, f1 = f1, max(f1, f0 + x * cnt[x])
        return f1
    def solve2a(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        keys = sorted(cnt.keys())
        @cache
        def dfs(i: int) -> int:
            if i < 0:
                return 0
            if i and keys[i] == keys[i-1] + 1: # 不能偷前一家
                return max(dfs(i-1), dfs(i-2) + keys[i] * cnt[keys[i]])
            return dfs(i-1) + keys[i] * cnt[keys[i]]
        return dfs(len(keys) - 1)
    def solve2b(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        keys = sorted(cnt.keys())
        n = len(keys)
        dp = [0] * (n + 1)
        dp[1] = keys[0] * cnt[keys[0]]
        for i in range(2, n + 1):
            if keys[i-1] == keys[i-2] + 1:
                dp[i] = max(dp[i-1], dp[i-2] + keys[i-1] * cnt[keys[i-1]])
            else:
                dp[i] = dp[i-1] + keys[i-1] * cnt[keys[i-1]]
        return dp[n]
    def solve2c(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        keys = sorted(cnt.keys())
        f0, f1 = 0, 0
        for i, k in enumerate(keys):
            if i and k == keys[i-1] + 1:
                f0, f1 = f1, max(f1, f0 + k * cnt[k])
            else:
                f0, f1 = f1, f1 + k * cnt[k]
        return f1
# @lc code=end
sol = Solution()
print(sol.deleteAndEarn([3,4,2])) # 6
print(sol.deleteAndEarn([2,2,3,3,3,4])) # 9
print(sol.deleteAndEarn([3,1])) # 4
#
# @lcpr case=start
# [3,4,2]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,3,3,3,4]\n
# @lcpr case=end

#

