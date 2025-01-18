# @algorithm @lc id=55 lang=python3 
# @title jump-game


from en.Python3.mod.preImport import *
# @test([2,3,1,1,4])=true
# @test([3,2,1,0,4])=false
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        rightmost = 0 # 最遠能跳到的位置
        for idx, jump in enumerate(nums):
            rightmost = max(rightmost, idx + jump) # 當前位置能跳到的最遠位置
            if rightmost == (n-1): # 已經能跳到終點了
                return True
            if rightmost <= idx: # 不能跳到更遠的位置了
                return False
        return True