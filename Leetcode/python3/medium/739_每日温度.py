#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#
import sys 
sys.path.append("..")
from preImport import *
# @lc code=start
class Solution:
    """
        Monotonic stack
        在Stack存放的是index，但對應的element是遞減的
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0 for _ in range(n)] # 初始化答案為0，即無法在右側找到比當前element大的element
        st = []
        for idx, temp in enumerate(temperatures):
            # 取出stack中比當前element小的element，計算距離後即為答案
            while st and temp > temperatures[st[-1]]: 
                ans[st[-1]] = idx - st[-1]
                st.pop()
            st.append(idx)
        return ans
# @lc code=end

