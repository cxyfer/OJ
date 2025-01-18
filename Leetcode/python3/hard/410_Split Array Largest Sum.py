#
# @lc app=leetcode id=410 lang=python3
# @lcpr version=30204
#
# [410] Split Array Largest Sum
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
"""
    1. Binary Search
    最小化最大值

    2. Dynamic Programming
"""
class Solution1:
    def splitArray(self, nums: List[int], k: int) -> int:
        # 是否可以將 nums 分成 k 個子陣列，使得每個子陣列的和都小於等於 d
        def check(d: int) -> bool:
            s, cnt = 0, 1
            for x in nums:
                if s + x > d:
                    cnt += 1
                    s = x
                else:
                    s += x
            return cnt <= k
        
        left, right = max(nums), sum(nums)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

class Solution2a:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0))

        @cache
        def dfs(i: int, j: int) -> int: # 前 i 個數字分成 j 個子陣列，所得到最大和的最小值
            if j == 1:
                return s[i]
            if j > i: # 不能分成 j 個子陣列
                return 10**10
            res = 10**10
            for x in range(i): # 枚舉上一段的結尾是第 x 個數字
                res = min(res, max(dfs(x, j - 1), s[i] - s[x]))
            return res
        
        return dfs(n, k)

class Solution2b:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        s = list(accumulate(nums, initial=0)) # prefix sum

        dp = [[10**10] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                for x in range(i):
                    dp[i][j] = min(dp[i][j], max(dp[x][j - 1], s[i] - s[x]))
        return dp[n][k]

# class Solution(Solution1):
class Solution(Solution2a):
# class Solution(Solution2b):
    pass
# @lc code=end

sol = Solution()
print(sol.splitArray([7,2,5,10,8], 2)) # 18
print(sol.splitArray([1,2,3,4,5], 2)) # 9
print(sol.splitArray([1,4,4], 3)) # 4

#
# @lcpr case=start
# [7,2,5,10,8]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n2\n
# @lcpr case=end

#

