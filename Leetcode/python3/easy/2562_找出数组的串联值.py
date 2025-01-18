#
# @lc app=leetcode.cn id=2562 lang=python3
#
# [2562] 找出数组的串联值
#
from preImport import *
# @lc code=start
class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        ans = 0
        while (left <= right):
            if left == right:
                ans += nums[left]
            else:
                ans += int(str(nums[left]) + str(nums[right]))
            left += 1
            right -= 1
        return ans
# @lc code=end
sol = Solution()
print(sol.findTheArrayConcVal([7,52,2,4])) # 596
print(sol.findTheArrayConcVal([5,14,13,8,12])) # 673
print(sol.findTheArrayConcVal([1])) # 1


