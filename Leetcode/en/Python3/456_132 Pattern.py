# @algorithm @lc id=456 lang=python3 
# @title 132-pattern


from en.Python3.mod.preImport import *
# @test([1,2,3,4])=false
# @test([3,1,4,2])=true
# @test([-1,3,2,0])=true
# @test([-2,1,1])=false

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
            if nums[i] > max_k:
                stack.append(nums[i])
        return False