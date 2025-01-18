#
# @lc app=leetcode id=3098 lang=python3
# @lcpr version=30204
#
# [3098] Find the Sum of Subsequence Powers
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def sumOfPowers(self, nums: List[int], k: int) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        nums.sort()
        # 由後往前考慮，當前考慮的數為 nums[i]、剩餘可選 j 個數
        # 上一個選的數字為 pre、目前選擇的子序列的最小差值為 min_diff
        @cache # Memoization
        def dfs(i, j, pre, min_diff) -> int:
            if j > i + 1:
                return 0
            if j == 0:
                return min_diff
            res1 = dfs(i-1, j, pre, min_diff) # 不選
            res2 = dfs(i-1, j-1, nums[i], min(min_diff, pre-nums[i])) # 選
            return (res1 + res2) % MOD
        return dfs(n-1, k, float('inf'), float('inf'))
# @lc code=end



#
# @lcpr case=start
# [1,2,3,4]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,2]\n2\n
# @lcpr case=end

# @lcpr case=start
# [4,3,-1]\n2\n
# @lcpr case=end

#

