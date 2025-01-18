# @algorithm @lc id=1489 lang=python3 
# @title pizza-with-3n-slices


from en.Python3.mod.preImport import *
# @test([1,2,3,4,5,6])=10
# @test([8,9,8,6,1,1])=16
class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        # DP
        # 此問題等於在Array中選n個不相鄰的數字，使得和最大
        def cal(nums: List[int]) -> int:
            m = len(nums)
            n = (m+1) // 3
            # dp[i][j] 表示前i個數字中選j個的最大和
            dp = [[0] * (n+1) for _ in range(m+1)]
            for i in range(1, m+1):
                for j in range(1, n+1):
                    # 1. 不選第i個 或 2. 選第i個
                    dp[i][j] = max(dp[i-1][j], (dp[i-2][j-1] if i >= 2 else 0) + nums[i-1])
            return dp[m][n]
        # 因為是環狀，所以第一個和最後一個不能同時選
        x = cal(slices[1:]) # 選第一個
        y = cal(slices[:-1]) # 選最後一個
        return max(x, y)
        