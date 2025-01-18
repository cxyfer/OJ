# @algorithm @lc id=2530 lang=python3 
# @title minimize-maximum-of-array


from en.Python3.mod.preImport import *
# @test([3,7,1,6])=5
# @test([10,1])=10
class Solution:
    """
        Binary search
        二分答案
    """
    def minimizeArrayValue(self, nums: List[int]) -> int:
        n = len(nums)

        def check(mx: int) -> bool: # 檢查是否能將數組中的最大值降至 mx
            added = 0 # 額外增加的值
            for i in range(n - 1, 0, -1): # 由後往前遍歷
                added = max(nums[i] + added - mx, 0) 
            return nums[0] + added <= mx
        
        # return bisect_left(range(max(nums)), True, key=check)
        left, right = 0, max(nums) # [left, right]
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left