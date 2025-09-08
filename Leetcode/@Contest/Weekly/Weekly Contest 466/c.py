import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

from typing import List

class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        st = []
        pre = [-1] * n
        for i, x in enumerate(nums):
            while st and nums[st[-1]] <= x:
                st.pop()
            if st:
                pre[i] = st[-1]
            st.append(i)
        st = []
        suf = [-1] * n
        for i in range(n - 1, -1, -1):
            x = nums[i]
            while st and nums[st[-1]] <= x:
                st.pop()
            if st:
                suf[i] = st[-1]
            st.append(i)
        ans = 0
        for p, s in zip(pre, suf):
            ans += (p != -1) and (s != -1)
        return ans


sol = Solution()
print(sol.bowlSubarrays([2,5,3,1,4]))  # 2
print(sol.bowlSubarrays([5,1,2,3,4]))  # 3
print(sol.bowlSubarrays([1000000000,999999999,999999998]))  # 0