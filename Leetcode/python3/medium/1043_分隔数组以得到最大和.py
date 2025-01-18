#
# @lc app=leetcode.cn id=1043 lang=python3
#
# [1043] 分隔数组以得到最大和
#
from preImport import *
# @lc code=start
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        return self.solve1(arr, k)
    def solve1(self, arr: List[int], k: int) -> int:
        n = len(arr)
        @cache
        def dfs(i: int) -> int:
            res = 0 # result
            mx = 0 # max value in the current window
            for j in range(i, min(i + k, n)):
                mx = max(mx, arr[j]) # update max value of the current window
                res = max(res, mx * (j - i + 1) + dfs(j + 1)) # update result
            return res
        return dfs(0)
    def solve2(self, arr: List[int], k: int) -> int:
        n = len(arr)
        @cache
        def dfs(i: int) -> int:
            res = 0 # result
            mx = 0 # max value in the current window
            for j in range(0, min(k, n - i) + 1):
                mx = max(mx, arr[i + j])
        return dfs(0)
# @lc code=end

