#
# @lc app=leetcode.cn id=1658 lang=python3
#
# [1658] 将 x 减到 0 的最小操作数
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        left, right = 0, n-1
        lsum, rsum = 0, 0
        while left < n and lsum < x: # count left side first
            lsum += nums[left]
            left += 1
        ans = float('inf')
        if lsum == x: # can select all from left
            ans = left
        while left <= right and left >= 0 and right >= 0: # this line should be corrected to left > 0, instead of left >= 0
            lsum -= nums[left-1] # remove rightmost element from left
            left -= 1
            while lsum + rsum < x and right >= 0: # make lsun + rsum >= x
                rsum += nums[right]
                right -= 1
            if lsum + rsum == x: # update ans
                ans = min(ans, left + n - right - 1)
        return ans if ans != float('inf') else -1
# @lc code=end

sol = Solution()
print(sol.minOperations([1,1,4,2,3],6)) # 3
exit()
print(sol.minOperations([1,1],3)) # -1
print(sol.minOperations([1,1,4,2,3],6)) # 3
print(sol.minOperations([1,1,4,2,3],5)) # 2

print(sol.minOperations([5,6,7,8,9],4)) # -1
print(sol.minOperations([3,2,20,1,1,3],10)) # 5

