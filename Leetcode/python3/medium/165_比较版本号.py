#
# @lc app=leetcode.cn id=165 lang=python3
#
# [165] 比较版本号
#
from preImport import *
# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = list(map(int, version1.split('.')))
        version2 = list(map(int, version2.split('.')))
        # n = max(len(version1), len(version2)) # 保證兩個陣列等長
        # version1 += [0] * (n - len(version1)) 
        # version2 += [0] * (n - len(version2))
        # for v1, v2 in zip(version1, version2):
        for v1, v2 in zip_longest(version1, version2, fillvalue=0): # 保證兩個陣列等長
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0
# @lc code=end

