#
# @lc app=leetcode.cn id=1475 lang=python3
#
# [1475] 商品折扣后的最终价格
#
from en.Python3.mod.preImport import *
from collections import deque
# @lc code=start
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
# @lc code=end

