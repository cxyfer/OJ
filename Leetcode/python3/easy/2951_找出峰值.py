#
# @lc app=leetcode.cn id=2951 lang=python3
#
# [2951] 找出峰值
#
from preImport import *
# @lc code=start
class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        n = len(mountain)
        ans = []
        for i in range(1, n-1):
            if mountain[i] > mountain[i-1] and mountain[i] > mountain[i+1]:
                ans.append(i)
        return ans
# @lc code=end

