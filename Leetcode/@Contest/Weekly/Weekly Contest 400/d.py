import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    """
        Same to 1521. Find a Value of a Mysterious Function Closest to Target
        AND 只會讓數字變小，所以可以用 Stack 來保存所有可能的 AND 結果
    """
    def minimumDifference(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ans = float("inf")
        st = []
        for x in nums:
            st2 = [x]
            for y in st:
                if y & x != st2[-1]:
                    st2.append(y & x)
            st = st2
            for y in st:
                ans = min(ans, abs(y - k))
        return ans
    
sol = Solution()
print(sol.minimumDifference([1,2,4,5], 3)) # 1
print(sol.minimumDifference([1,2,1,2], 2)) # 0
print(sol.minimumDifference([1], 10)) # 9
print(sol.minimumDifference([5,13,90,92,49], 10)) # 2