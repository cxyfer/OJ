import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

"""
Q3: 分類討論
由於可以 reverse，所以除了直接透過 rotate 得到**遞增**陣列外，也能透過 rotate 得到**遞減**陣列後，再 reverse 後得到遞增陣列。
此外，雖然題目只能 rotate left 和 reverse，但可以透過 reverse + rotate left + reverse 的方式達成 rotate right。

先判定能否達成，做過 2026-05-23 的每日一題 1752. Check if Array Is Sorted and Rotated 的應該對此不陌生，
只要在循環陣列中，遞增和遞減的轉折點都不超過 1 個就可以達成。

接著考慮答案：
- 如果要得到遞增陣列，可以把最小值左移到開頭、或是把最大值右移到結尾後；
- 反之如果要得到遞減陣列，可以把最大值左移到開頭、或是把最小值右移到結尾，最後再加上一次翻轉
  - 但在後者的過程中，最小值會在翻轉後先被移動到開頭，因此後面兩次翻轉是多餘的
"""

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        
        cnt1 = cnt2 = 0
        for i, x in enumerate(nums):
            if nums[i] > nums[(i + 1) % n]:
                cnt1 += 1
            else:  # nums 是排列，因此不會有相等的情況
                cnt2 += 1
                
        if cnt1 > 1 and cnt2 > 1:
            return -1

        rev = list(reversed(nums))

        ans = inf
        mn = min(nums)
        mx = max(nums)
        if cnt1 <= 1:  # 可以透過 rotate 得到遞增陣列
            idx = nums.index(mn)
            ans = min(ans, idx)  # 把最小值移動到開頭
            idx = rev.index(mx)
            ans = min(ans, idx + 2)  # 翻轉後把最大值移動到開頭，最後再翻轉一次
        if cnt2 <= 1:  # 可以透過 rotate 得到遞減陣列
            idx = nums.index(mx)
            ans = min(ans, idx + 1)  # 把最大值移動到開頭後翻轉
            idx = rev.index(mn)
            ans = min(ans, idx + 1)  # 翻轉後把最小值移動到開頭
        return ans