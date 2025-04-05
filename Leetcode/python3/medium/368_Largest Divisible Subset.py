#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
DP: Similar to Longest Increasing Subsequence (LIS)

重要前提：往一個 Largest Divisible Subset (LDS) 中加入一個數時，**不需檢查所有數**
假設一個 LDS 為 {a, b, c}，其中 a < b < c，則只要滿足以下任一條件，即可將 x 加入 LDS
1. x | a
2. c | x

至此便可將此問題轉為 Longest Increasing Subsequence (LIS) 問題
"""
# @lc code=start
class Solution1:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        # f[x] 表示以 x 結尾的 Largest Divisible Subset
        f = {x: [x] for x in nums}
        for i, x in enumerate(nums):
            # 枚舉 x 的前一個數 y = nums[j]，若 y | x，則 ∀u, u ∈ f[y] -> u | x
            for j in range(i):
                if x % nums[j] == 0:
                    f[x] = max(f[x], f[nums[j]] + [x], key=len)
        return max(f.values(), key=len)

class Solution2:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        # f[i] 表示以 nums[i] 結尾的 Largest Divisible Subset 大小
        f = [1] * n
        mx = 1
        for i, x in enumerate(nums):
            # 枚舉 x 的前一個數 y = nums[j]，若 y | x，則 ∀u, u ∈ f[y] -> u | x
            for j in range(i):
                if x % nums[j] == 0 and f[i] < f[j] + 1:
                    f[i] = f[j] + 1
            mx = max(mx, f[i])  # 更新最大的 LDS 大小
        # 從後往前找，找到最大的 LDS
        ans = []
        for i in range(n - 1, -1, -1):
            if f[i] == mx and (not ans or ans[-1] % nums[i] == 0):
                ans.append(nums[i])
                mx -= 1
        return ans

# Solution = Solution1
Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.largestDivisibleSubset([3,4,16,8])) # [4,8,16]
