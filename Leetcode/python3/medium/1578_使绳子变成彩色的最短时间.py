#
# @lc app=leetcode.cn id=1578 lang=python3
#
# [1578] 使绳子变成彩色的最短时间
#
from preImport import *
# @lc code=start
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        n = len(colors)
        ans = 0
        i = 0
        while i < n: # 分組循環
            st = i
            mx = s = neededTime[i] # 當前組內的總和, 最大值
            while i < n - 1 and colors[i] == colors[i + 1]: # 同一組
                i += 1
                mx = max(mx, neededTime[i]) # 更新組內最大值
                s += neededTime[i] # 組內總和
            if i > st: 
                ans += (s - mx)
            i += 1
        return ans
# @lc code=end

