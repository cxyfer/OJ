from bisect import *
from collections import *
from functools import *
from heapq import *
from itertools import *
from math import *
from operator import *
from random import *
from string import *
from typing import *

del pow

"""
Q4. ||Manacher||
首先注意到 nums[i] >= 1，因此對於固定的迴文中心，可以盡可能的擴展。
而 Manacher 可以計算以某個位置為迴文中心的最長迴文子串的長度，
得到對應的原始陣列的左右邊界後，用前綴和計算區間和即可。

Manacher 模板：https://leetcode.cn/circle/discuss/SJFwQI/
"""

"""
    
"""

class Manacher:
    def __init__(self, s) -> None:
        self.s = s
        if isinstance(s, str):
            self.t = '#'.join("^" + s + "$")
        elif isinstance(s, list):
            self.t = '#'.join(['^'] + s + ['$'])
        else:
            raise ValueError("s must be a string or a list")
        
        self.halfLen = [0] * (len(self.t) - 2)
        self.halfLen[1] = 1
        boxM = boxR = 0
        self.max_i = 0 # 最長回文子字串的中心位置
        for i in range(2, len(self.halfLen)):
            hl = 1
            if i < boxR:
                hl = min(self.halfLen[boxM * 2 - i], boxR - i)
            while self.t[i - hl] == self.t[i + hl]:
                hl += 1
                boxM, boxR = i, i + hl
            self.halfLen[i] = hl
            if hl > self.halfLen[self.max_i]:
                self.max_i = i

    # 判斷 s[l:r] 是否為回文字串
    def isPalindrome(self, l: int, r: int) -> bool:
        return self.halfLen[l + r + 1] > r - l
    
    # 獲取最長回文子字串的長度
    def getMaxPalindromeLength(self) -> int:
        return self.halfLen[self.max_i] - 1
    
    # 獲取最長回文子字串
    def getMaxPalindrome(self) -> str:
        hl = self.halfLen[self.max_i]
        return self.s[(self.max_i - hl) // 2:(self.max_i + hl) // 2 - 1]

class Solution:
    def getSum(self, nums: List[int]) -> int:
        # Manacher ?

        t = [-1]
        for x in nums:
            t.append(-2)
            t.append(x)
        t.append(-2)
        t.append(-3)
        
        halfLen = [0] * (len(t) - 2)
        halfLen[1] = 1
        boxM = boxR = 0
        for i in range(2, len(halfLen)):
            hl = 1
            if i < boxR:
                hl = min(halfLen[boxM * 2 - i], boxR - i)
            while t[i - hl] == t[i + hl]:
                hl += 1
                boxM, boxR = i, i + hl
            halfLen[i] = hl

        ans = 0
        s = list(accumulate(nums, initial=0))
        for i in range(2, len(halfLen)):
            hl = halfLen[i]

            l = (i - hl) // 2
            r = (i + hl) // 2 - 1
            if l < r:
                ans = max(ans, s[r] - s[l])
        return ans

sol = Solution()
print(sol.getSum([10, 10]))  # 20
print(sol.getSum([1, 2, 3, 2, 1, 5, 6]))  # 9
print(sol.getSum([7,1,2,1,7,3,4,3,4]))  # 18
print(sol.getSum([1,2,3,4,5]))  # 5
print(sol.getSum([1000]))  # 1000