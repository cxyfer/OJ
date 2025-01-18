# @algorithm @lc id=3106 lang=python3 
# @title length-of-the-longest-subsequence-that-sums-to-target


from en.Python3.mod.preImport import *
# @test([1,2,3,4,5],9)=3
# @test([4,1,3,2,1,5],7)=4
# @test([1,1,5,4,5],3)=-1
class Solution:
    """
        Dynamic programming
        dp[i][j] = length of longest subsequence of nums[:i] that sums up to j
    """
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [[0 for _ in range(target+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(target+1):
                dp[i][j] = dp[i-1][j]
            for j in range(target+1):
                if j - nums[i-1] >= 0 and dp[i-1][j-nums[i-1]] > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j-nums[i-1]] + 1)
            if nums[i-1] <= target:
                dp[i][nums[i-1]] = max(dp[i][nums[i-1]], 1)
        # for line in dp:
        #     print(line)
        return dp[n][target] if dp[n][target] > 0 else -1
    
sol = Solution()
print(sol.lengthOfLongestSubsequence([1,2,3,4,5], 9)) # 3
print(sol.lengthOfLongestSubsequence([4,1,3,2,1,5], 7)) # 4
print(sol.lengthOfLongestSubsequence([1,1,5,4,5], 3)) # -1
print(sol.lengthOfLongestSubsequence([2,3,5], 5)) # 2