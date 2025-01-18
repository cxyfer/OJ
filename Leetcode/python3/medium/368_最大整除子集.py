#
# @lc app=leetcode.cn id=368 lang=python3
#
# [368] 最大整除子集
#
from preImport import *
# @lc code=start
class Solution:
    """
        DP, similar to LIS
        令 cnt[num] 表示以 num 結尾的最大整除子集
    """
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        cnt = defaultdict(list) # cnt[num] 表示以 num 結尾的最大整除子集
        for i, num in enumerate(nums):
            cnt[num] = [num] # 以 num 結尾最小整除子集為 [num]
            for j in range(i):
                if num % nums[j] == 0 and len(cnt[nums[j]]) + 1 > len(cnt[num]): # cnt[nums[j]] 加上 nums[i] 後能構成更長的整除子集
                    cnt[num] = cnt[nums[j]] + [num]
        return max(cnt.values(), key=len) # 返回最長的整除子集
# @lc code=end
# @test([1,2,3])=[1,2]
# @test([1,2,4,8])=[1,2,4,8]
sol = Solution()
print(sol.largestDivisibleSubset([1,2,3])) # [1,2]
print(sol.largestDivisibleSubset([1,2,4,8])) # [1,2,4,8]