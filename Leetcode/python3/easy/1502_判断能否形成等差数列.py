#
# @lc app=leetcode.cn id=1502 lang=python3
#
# [1502] 判断能否形成等差数列
#
from preImport import *
# @lc code=start
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        n = len(arr)
        arr.sort()
        d = (arr[-1] - arr[0]) // (n-1)
        for i in range(1, n):
            if arr[i] - arr[i-1] != d:
                return False
        return True
# @lc code=end

