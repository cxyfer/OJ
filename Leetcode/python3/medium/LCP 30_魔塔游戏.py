#
# @lc app=leetcode.cn id=LCP 30 lang=python3
# @lcpr version=30116
#
# [LCP 30] 魔塔游戏
#


# @lcpr-template-start
import math
from math import *
from typing import *
from collections import *
from functools import *
from itertools import *
from bisect import *
from heapq import *
# @lcpr-template-end
# @lc code=start
class Solution:
    """
        模擬 + Greedy + Heap
        遇到血量為負的時候，基於貪心原則，把前面的負數中最小的那個扔到後面去。
    """
    def magicTower(self, nums: List[int]) -> int:
        if sum(nums) < 0: # 先處理總和小於0的情況
            return -1
        
        cur, ans = 1, 0 # 當前血量、調整次數
        hp = [] # Min Heap

        for x in nums:
            cur += x
            if x < 0: # 負數進堆
                heappush(hp, x)
            if cur <= 0: # 血量不夠
                cur -= heappop(hp) # 選擇一個負數扔到最後
                ans += 1
        return ans
# @lc code=end



#
# @lcpr case=start
# [100,100,100,-250,-60,-140,-50,-50,100,150]`>\n
# @lcpr case=end

# @lcpr case=start
# [-200,-300,400,0]`>\n
# @lcpr case=end

#

