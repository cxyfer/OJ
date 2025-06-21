import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        st = []
        for x in nums:
            if x == 0:
                st.clear()
                continue
            while st and st[-1] > x:
                st.pop()
            if st and st[-1] == x:
                continue
            st.append(x)
            ans += 1
        return ans


sol = Solution()