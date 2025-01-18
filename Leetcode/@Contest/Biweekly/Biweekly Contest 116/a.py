from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for l in range(1, n+1):
            for i in range(n-l+1):
                ans += len(set(nums[i:i+l]))** 2
        return ans
sol = Solution()
print(sol.sumCounts([1,2,1])) # 15