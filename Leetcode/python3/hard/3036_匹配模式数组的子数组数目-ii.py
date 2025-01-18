#
# @lc app=leetcode.cn id=3036 lang=python3
#
# [3036] 匹配模式数组的子数组数目 II
#
from preImport import *
# @lc code=start
class Solution:
    """
        Longest Common Prefix (LCP)
        - KMP
        - Z Function
    """
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        target = [(nums[i] < nums[i+1]) - (nums[i] > nums[i+1]) for i in range(len(nums)-1)]
        
        s = pattern + [9] + target
        m, n = len(pattern), len(s)
        z = [0] * n # length of LCP
        l, r = 0, 0
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                l, r = i, i + z[i] - 1
                z[i] += 1
        return sum(z[i] >= m for i in range(m, n))
   
# @lc code=end
# @test([1,2,3,4,5,6],[1,1])=4
# @test([1,4,4,1,3,5,5,3],[1,0,-1])=2
sol = Solution()
print(sol.countMatchingSubarrays([1,2,3,4,5,6],[1,1])) # 4
print(sol.countMatchingSubarrays([1,4,4,1,3,5,5,3],[1,0,-1])) # 2
