#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#
from en.Python3.mod.preImport import *
# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
            Greedy
        """
        n = len(nums)
        rightmost = 0 # 最遠能跳到的位置
        for idx, jump in enumerate(nums):
            rightmost = max(rightmost, idx + jump) # 當前位置能跳到的最遠位置
            if rightmost == (n-1): # 已經能跳到終點了
                return True
            if rightmost <= idx: # 不能跳到更遠的位置了
                return False
        return True

# @lc code=end

