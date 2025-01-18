#
# @lc app=leetcode.cn id=682 lang=python3
#
# [682] 棒球比赛
#
from preImport import *
# @lc code=start
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        for op in operations:
            if op == "D":
                st.append(st[-1] * 2)
            elif op == "+":
                st.append(st[-1] + st[-2])
            elif op == "C":
                st.pop()
            else:
                st.append(int(op))
        return sum(st)
# @lc code=end

