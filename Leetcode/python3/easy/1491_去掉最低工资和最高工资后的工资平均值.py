#
# @lc app=leetcode.cn id=1491 lang=python3
#
# [1491] 去掉最低工资和最高工资后的工资平均值
#
from preImport import *
# @lc code=start
class Solution:
    def average(self, salary: List[int]) -> float:
        n = len(salary)
        ans = 0
        mx, mn = float('-inf'), float('inf')
        for num in salary:
            mx = max(mx, num)
            mn = min(mn, num)
            ans += num
        return (ans-mx-mn)/(n-2)
# @lc code=end

