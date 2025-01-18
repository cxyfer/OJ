#
# @lc app=leetcode id=377 lang=python3
# @lcpr version=30201
#
# [377] Combination Sum IV
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # return self.solve1(nums, target)
        return self.solve2(nums, target)
    def solve1(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target+1)] # dp[i] 表示和為 i 的組合數
        dp[0] = 1
        for cur in range(1, target+1):
            for num in nums:
                if cur >= num:
                    dp[cur] += dp[cur-num]
        return dp[target]
    def solve2(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(i: int):
            if i == 0:
                return 1
            return sum(dfs(i-x) for x in nums if i >= x)
        return dfs(target)
# @lc code=end



#
# @lcpr case=start
# [1,2,3]\n4\n
# @lcpr case=end

# @lcpr case=start
# [9]\n3\n
# @lcpr case=end

#

