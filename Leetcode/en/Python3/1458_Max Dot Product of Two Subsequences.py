# @algorithm @lc id=1569 lang=python3 
# @title max-dot-product-of-two-subsequences


from en.Python3.mod.preImport import *
# @test([2,1,-2,5],[3,0,-6])=18
# @test([3,-2],[2,-6,7])=21
# @test([-1,-1],[1,1])=-1
class Solution:
    """
        Dynamic Programming
    """
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        # dp[i][j] 表示 nums1[:i] 和 nums2[:j] 的最大dot product
        dp = [[float("-inf")]*(n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                pij = nums1[i-1] * nums2[j-1] # product of nums1[i] and nums2[j]
                dp[i][j] = max(pij, dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + pij)
        return dp[-1][-1]