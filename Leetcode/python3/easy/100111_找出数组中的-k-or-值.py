#
# @lc app=leetcode.cn id=100111 lang=python3
#
# [100111] 找出数组中的 K-or 值
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
    def findKOr(self, nums: List[int], k: int) -> int:
        cnt = Counter()
        for num in nums:
            idx = 0
            while num:
                cnt[idx] += num & 1
                num >>= 1
                idx += 1
        ans = 0
        for b in cnt.keys():
            ans += (1 << b) if cnt[b] >= k else 0
        return ans
# @lc code=end
sol = Solution()
print(sol.findKOr([7,12,9,8,9,15], 4)) # 9
print(sol.findKOr([2,12,1,11,4,5], 6)) # 0
print(sol.findKOr([10,8,5,9,11,6,8], 1)) #15
