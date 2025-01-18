# @algorithm @lc id=53 lang=python3 
# @title maximum-subarray


from en.Python3.mod.preImport import *
# @test([-2,1,-3,4,-1,2,1,-5,4])=6
# @test([1])=1
# @test([5,4,-1,7,8])=23
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.solveByDP(nums)

    """
        Dynamic Programming
        Time: O(n)
        - dp[i] 表示 包含 nums[i] 的最大子數組和
        - dp[i] = max(dp[i-1] + nums[i], nums[i])
    """
    def solveByDP(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        for i in range(1, n):
            # 取nums[i-1] 或 不取nums[i-1]，從nums[i]開始重新計算
            dp[i] = max(nums[i], dp[i-1] + nums[i])
        return max(dp)
    """
        Divide and Conquer
        Time: O(nlogn)
    """
    def solveByDC(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: # base case
            return nums[0] 
        # Divide to 2 subproblems
        l_max = self.maxSubArray(nums[:n//2])
        r_max = self.maxSubArray(nums[n//2:])

        # Combine
        c_max_l, c_max_r = nums[n//2-1], nums[n//2]
        tmp_l = tmp_r = 0 # 分別從中間往左右兩邊加，找出左右的最大值
        for i in range(n//2-1, -1, -1):
            tmp_l += nums[i]
            c_max_l = max(c_max_l, tmp_l)
        for i in range(n//2, n):
            tmp_r += nums[i]
            c_max_r = max(c_max_r, tmp_r)
        c_max = c_max_l + c_max_r
        return max(l_max, r_max, c_max) # 返回最大值
