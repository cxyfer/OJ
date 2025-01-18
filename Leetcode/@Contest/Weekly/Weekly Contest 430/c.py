import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def numberOfSubsequences(self, nums: List[int]) -> int:
        n = len(nums)
        
        left_pairs = defaultdict(list)
        for p in range(n - 2):
            for r in range(p + 2, n):
                prod = nums[p] * nums[r]
                left_pairs[prod].append((p, r))
        
        right_map = defaultdict(lambda: defaultdict(list))
        for q in range(n - 2):
            for s in range(q + 2, n):
                prod = nums[q] * nums[s]
                right_map[prod][q].append(s)
        
        for prod in right_map:
            for q, s_list in right_map[prod].items():
                s_list.sort()
        
        ans = 0
        for prod, pairs in left_pairs.items():
            if prod not in right_map:
                continue
            q_dict = right_map[prod]
            for (p, r) in pairs:
                q_min = p + 2
                q_max = r - 2
                if q_min > q_max:
                    continue
                for q, s_list in q_dict.items():
                    if q < q_min or q > q_max:
                        continue
                    idx = bisect_left(s_list, r + 2)
                    ans += (len(s_list) - idx)
        return ans

sol = Solution()
print(sol.numberOfSubsequences([1,2,3,4,3,6,1])) # 1
print(sol.numberOfSubsequences([3,4,3,4,3,4,3,4])) # 3
