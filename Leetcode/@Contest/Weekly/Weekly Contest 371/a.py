from typing import List

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                x, y = nums[i], nums[j]
                if abs(x-y) <= min(x, y):
                    ans = max(ans, x^y)
        return ans

sol = Solution()
print(sol.maximumStrongPairXor([1,2,3,4,5])) # 7
print(sol.maximumStrongPairXor([10,100])) # 0
print(sol.maximumStrongPairXor([5,6,25,30])) # 7
print(sol.maximumStrongPairXor([1,2,2,1,2])) # 3