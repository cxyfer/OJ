# @algorithm @lc id=41 lang=python3 
# @title first-missing-positive


from en.Python3.mod.preImport import *
# @test([1,2,0])=3
# @test([3,4,-1,1])=2
# @test([7,8,9,11,12])=1
class Solution:
    """
        原地哈希
        答案必定在[1, n+1]這n個數之間
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        # 1. 將負數或0標記為n+1
        for i in range(n):
            if nums[i] <= 0: 
                nums[i] = n + 1
        # 2. 將出現過的數字標記為負數
        for i in range(n): 
            num = abs(nums[i]) # 取絕對值，避免重複被標記
            if num <= n: # 對[1, n]之間的數字進行標記
                nums[num-1] = -abs(nums[num-1])
        # 3. 找到第一個沒有被標記的數字
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1 # 如果都被標記了，則答案為n+1