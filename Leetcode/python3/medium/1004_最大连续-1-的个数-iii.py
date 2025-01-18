#
# @lc app=leetcode.cn id=1004 lang=python3
#
# [1004] 最大连续1的个数 III
#
from preImport import *
# @lc code=start
class Solution:
    """
        Sliding window
        將題目轉換成找一個最長的子串，使得子串中0的個數不超過k個
    """
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        cnt = 0 # 0的個數
        ans = 0
        for right in range(n):
            if nums[right] == 0:
                cnt += 1
            while cnt > k:
                if nums[left] == 0:
                    cnt -= 1
                left += 1
            ans = max(ans, right - left + 1)
        return ans
# @lc code=end

