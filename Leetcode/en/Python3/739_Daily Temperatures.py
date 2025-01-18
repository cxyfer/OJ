# @algorithm @lc id=739 lang=python3 
# @title daily-temperatures


from en.Python3.mod.preImport import *
from collections import deque
# @test([73,74,75,71,69,72,76,73])=[1,1,4,2,1,1,0,0]
# @test([30,40,50,60])=[1,1,1,0]
# @test([30,60,90])=[1,1,0]
class Solution:
    """
        Monotonic stack
        在Stack存放的是index，但對應的element是遞減的
    """
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = deque()
        stack.append(0) # 先把第一個element放進去
        ans = [0] * len(temperatures) # 初始化答案為0，即無法在右側找到比當前element大的element
        for i in range(1, n):
            # if temperatures[i] <= temperatures[stack[-1]]:
            #     stack.append(i)
            # else:
            #     # 一直取出stack中比當前element小的element，計算距離後即為答案
            #     while stack and temperatures[i] > temperatures[stack[-1]]:
            #         ans[stack[-1]] = i - stack[-1]
            #         stack.pop()
            #     stack.append(i)
            while stack and temperatures[i] > temperatures[stack[-1]]:
                ans[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
        return ans