# @algorithm @lc id=1570 lang=python3 
# @title final-prices-with-a-special-discount-in-a-shop


from en.Python3.mod.preImport import *
from collections import deque
# @test([8,4,6,2,3])=[4,2,4,2,3]
# @test([1,2,3,4,5])=[1,2,3,4,5]
# @test([10,1,1,6])=[9,0,1,6]
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # Monotonic stack
        # 題目要求的是右側第一個比當前element小的element，允許和當前element相等
        ans = prices[:]
        stack = deque() # Save index for prices
        stack.append(0)
        for i in range(1, len(prices)):
            while stack and prices[i] <= prices[stack[-1]]:
                ans[stack[-1]] -= prices[i]
                stack.pop()
            stack.append(i)
        return ans