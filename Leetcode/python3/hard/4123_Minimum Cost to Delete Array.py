#
# @lc app=leetcode id=4123 lang=python3
#
# [4123] Minimum Cost to Delete Array
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
Weekly Contest 529 - Q4

1. 狀態機 DP

為了包含整個陣列，0, n-1 兩個位置一定要選；
又為了滿足選擇的合法性，需要剩下 n - 2 個位置中選「偶數（包含 0）」個位置。

因此問題等價於在 n - 2 個位置中選「偶數」個位置的最小代價。
可以令 f[i][0/1] 表示在前 i 個數字選 偶數/奇數 個位置的最小代價。

2. 貪心
"""
# @lc code=start
class Solution1:
    def minCost(self, nums: list[int]) -> int:
        # nums[0] 和 nums[-1] 一定要選
        # 在中間 n - 2 個數字中選「偶數」個位置
        n = len(nums)

        # f[i][0/1] 表示在前 i 個數字選 偶數/奇數 個位置的最小代價
        # 考慮當前位置選或不選，有以下兩種轉移
        # f[i][0] = min(f[i-1][0], f[i-1][1] + nums[i])
        # f[i][1] = min(f[i-1][1], f[i-1][0] + nums[i])
        f0, f1 = 0, inf
        for i in range(1, n - 1):
            x = nums[i]
            f0, f1 = min(f0, f1 + x), min(f1, f0 + x)
        return nums[0] + nums[-1] + f0


class Solution2:
    def minCost(self, nums: list[int]) -> int:
        ans = nums[0] + nums[-1]

        A = sorted(nums[1:-1])
        for i in range(1, len(A), 2):
            if A[i - 1] + A[i] < 0:
                ans += A[i - 1] + A[i]
        return ans


class Solution3:
    def minCost(self, nums: list[int]) -> int:
        n = len(nums)

        neg_sum = neg_cnt = 0
        max_neg, min_pos = -inf, inf
        for i in range(1, n - 1):
            if nums[i] < 0:
                neg_sum += nums[i]
                neg_cnt += 1
                max_neg = max(max_neg, nums[i])
            else:
                min_pos = min(min_pos, nums[i])

        ans = nums[0] + nums[-1]
        if neg_cnt & 1 == 0:
            return ans + neg_sum
        return ans + min(neg_sum - max_neg, neg_sum + min_pos)


# Solution = Solution1
# Solution = Solution2
Solution = Solution3
# @lc code=end

