#
# @lc app=leetcode id=3040 lang=python3
# @lcpr version=30203
#
# [3040] Maximum Number of Operations With the Same Score II
#

# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        n = len(nums)
        @cache
        def dfs(target, i, j):  # (目標值, 左邊界, 右邊界)
            if i >= j:  # 區間內的數字小於2個
                return 0
            res = 0
            if nums[i] + nums[i + 1] == target:  # 使用左邊的兩個數字
                res = max(res, 1 + dfs(target, i + 2, j))
            if nums[j - 1] + nums[j] == target:  # 使用右邊的兩個數字
                res = max(res, 1 + dfs(target, i, j - 2))
            if nums[i] + nums[j] == target:  # 使用左右各一個數字
                res = max(res, 1 + dfs(target, i + 1, j - 1))
            return res
        res1 = dfs(nums[0] + nums[1], 2, n - 1)  # 使用左邊的兩個數字當作目標值
        res2 = dfs(nums[-2] + nums[-1], 0, n - 3)  # 使用右邊的兩個數字當作目標值
        res3 = dfs(nums[0] + nums[-1], 1, n - 2)  # 使用左右各一個數字之和當作目標值
        return 1 + max(res1, res2, res3)
# @lc code=end

sol = Solution()
print(sol.maxOperations([3, 2, 1, 2, 3, 4]))  # 3
print(sol.maxOperations([3, 2, 6, 1, 4]))  # 2
print(sol.maxOperations([2, 4, 3, 3, 5, 4, 9, 6]))  # 2

#
# @lcpr case=start
# [3,2,1,2,3,4]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,6,1,4]\n
# @lcpr case=end

#
