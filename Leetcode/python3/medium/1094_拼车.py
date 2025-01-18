#
# @lc app=leetcode.cn id=1094 lang=python3
#
# [1094] 拼车
#
from preImport import *
# @lc code=start
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        MAX_TO = max([trip[2] for trip in trips])

        diff = [0] * (MAX_TO + 1)
        for num, x, y in trips:
            diff[x] += num # from 
            diff[y] -= num # to
        
        cnt = 0 # 當前車上的人數
        for i in range(MAX_TO + 1):
            cnt += diff[i]
            if cnt > capacity: # 超載
                return False
        return True
# @lc code=end

