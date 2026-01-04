import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *
from operator import *
from collections import defaultdict
from typing import List

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for w in words:
            mp[w[0]].append(w)

        ans = []
        for top in words:
            for left in mp[top[0]]:
                if left == top:
                    continue
                for right in mp[top[3]]:
                    if right in [top, left]:
                        continue
                    for bottom in mp[left[3]]:
                        if bottom in [top, left, right]:
                            continue
                        if bottom[3] == right[3]:
                            ans.append([top, left, right, bottom])
        ans.sort()
        return ans


sol = Solution()
print(sol.wordSquares(["able","area","echo","also"]))  # [["able","area","echo","also"], ["area","able","also","echo"]]