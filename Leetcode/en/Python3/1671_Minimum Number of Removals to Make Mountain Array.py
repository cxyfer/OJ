# @algorithm @lc id=1766 lang=python3 
# @title minimum-number-of-removals-to-make-mountain-array


from en.Python3.mod.preImport import *
# @test([1,3,1])=0
# @test([2,1,1,5,6,2,3,1])=3
class Solution:
    """
        Longest Increasing Subsequence
        Similar to 300. Longest Increasing Subsequence
    """
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        # 1. Find LIS from left to right
        dp1 = [1] * n # dp[i] 表示由前往後，以 nums[i] 結尾的 LIS 長度
        for i in range(1, n): # 枚舉所有位置 i
            for j in range(i): # 枚舉 i 前面的所有位置 j
                if nums[j] < nums[i]: # nums[i] 可以接在 nums[j] 後面
                    if dp1[j] + 1 > dp1[i]: # 若可以得到更大的LIS長度，更新 dp[i] 和 prev[i]
                        dp1[i] = dp1[j] + 1
        # 2. Find LIS from right to left
        dp2 = [1] * n # dp[i] 表示由後往前，以 nums[i] 結尾的 LIS 長度
        for i in range(n-2, -1, -1): # 枚舉所有位置 i
            for j in range(n-1, i, -1): # 枚舉 i 後面的所有位置 j
                if nums[j] < nums[i]: # nums[i] 可以接在 nums[j] 前面
                    if dp2[j] + 1 > dp2[i]: # 若可以得到更大的LIS長度，更新 dp[i] 和 prev[i]
                        dp2[i] = dp2[j] + 1
        # 3. Find the maximum length of mountain array
        max_len = 0
        for i in range(1, n-1): # 以 i 為山頂
            # 若 dp1[i] == 1 代表山頂前沒有比它小的數字，根據定義，不是山形數組
            # 若 dp2[i] == 1 代表山頂後沒有比它小的數字，根據定義，不是山形數組
            if dp1[i] != 1 and dp2[i] != 1:
                max_len = max(max_len, dp1[i] + dp2[i] - 1)
        return n - max_len