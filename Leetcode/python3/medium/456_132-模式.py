#
# @lc app=leetcode.cn id=456 lang=python3
#
# [456] 132 模式
#
from preImport import *
# @lc code=start
class Solution:
    """
        Monotonic Stack
        i < j < k and nums[i] < nums[k] < nums[j]
        令 stack 保存 nums[k]，並且 stack 由下到上是單調遞減的
    """
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3: return False
        stack = [nums[-1]]
        max_k = float('-inf') # 用來記錄 nums[k] 的最大值
        for i in range(n-2, -1, -1):
            if nums[i] < max_k: 
                return True
            while stack and nums[i] >= stack[-1]:
                max_k = stack.pop()
            stack.append(nums[i])
        return False
        
# @lc code=end
sol = Solution()
print(sol.find132pattern([1,2,3,4])) # false
print(sol.find132pattern([3,1,4,2])) # true
print(sol.find132pattern([-1,3,2,0])) # true
