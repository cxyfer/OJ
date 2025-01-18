#
# @lc app=leetcode id=2044 lang=python3
# @lcpr version=30204
#
# [2044] Count Number of Maximum Bitwise-OR Subsets
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        mx = 0
        for x in nums:
            mx |= x
        ans = 0
        for s in range(1, 1 << n): # 枚舉所有子集
            cur = 0
            for i in range(n):
                if (s >> i) & 1:
                    cur |= nums[i]
            if cur == mx:
                ans += 1
        return ans
    
class Solution2:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        ans = mx = 0
        def dfs(i, cur):
            nonlocal ans, mx
            if i == len(nums):
                if cur == mx:
                    ans += 1
                elif cur > mx:
                    mx = cur
                    ans = 1
                return
            dfs(i + 1, cur | nums[i])
            dfs(i + 1, cur)
        dfs(0, 0)
        return ans
    
class Solution3:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        mx = 0
        for x in nums:
            mx |= x
        @cache # Memoization
        def dfs(i, cur):
            if i == n:
                return cur == mx
            return dfs(i + 1, cur) + dfs(i + 1, cur | nums[i])
        return dfs(0, 0)
    
class Solution4:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        mx = 0
        for x in nums:
            mx |= x
        # dp[i] 表示子集的 OR 值為 i 的子集數量
        dp = [0] * (1 << mx.bit_length())
        dp[0] = 1
        for x in nums:
            for i in range(mx, -1, -1):
                dp[i | x] += dp[i]
        return dp[mx]
    
# class Solution(Solution1):
# class Solution(Solution2):
# class Solution(Solution3):
class Solution(Solution4):
    pass   
# @lc code=end

sol = Solution()
print(sol.countMaxOrSubsets([3,1]))

#
# @lcpr case=start
# [3,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,2,2]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1,5]\n
# @lcpr case=end

#

