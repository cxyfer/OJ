#
# @lc app=leetcode id=3250 lang=python3
# @lcpr version=30204
#
# [3250] Find the Count of Monotonic Pairs I
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10 ** 9 + 7
        @cache
        def dfs(i: int, pre: int) -> int:
            if i == n:
                return 1
            res = 0
            for x in range(max(pre, 0), nums[i] + 1): # 枚舉 arr1 中這個位置可以填的數字
                y = nums[i] - x # 對應的 arr2 中的數字
                if y >= 0 and (pre == -1 or y <= (nums[i - 1] - pre)):
                    res += dfs(i + 1, x)
            return res % MOD
        return dfs(0, -1)
# @lc code=end

sol = Solution()
print(sol.countOfPairs([2,3,2])) # 4
print(sol.countOfPairs([5,5,5,5])) # 126

#
# @lcpr case=start
# [2,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [5,5,5,5]\n
# @lcpr case=end

#

