#
# @lc app=leetcode.cn id=997 lang=python3
#
# [997] 找到小镇的法官
#
from preImport import *
# @lc code=start
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indeg = [0] * (n + 1)
        outdeg = [0] * (n + 1)
        for a, b in trust:
            indeg[b] += 1
            outdeg[a] += 1
        for i in range(1, n + 1):
            if indeg[i] == n - 1 and outdeg[i] == 0:
                return i
        return -1
# @lc code=end

