import math
from typing import *
from collections import *
from functools import *
from heapq import *
from bisect import *
from itertools import *

class Solution:
    def countMentions(self, n: int, events: List[List[str]]) -> List[int]:
        ans = [0] * n
        off = [0] * n
        events.sort(key=lambda x: (int(x[1]), 0 if x[0] == 'OFFLINE' else 1))
        for (typ, ts, data) in events:
            ts = int(ts)
            if typ == "OFFLINE":
                uid = int(data)
                off[uid] = ts + 60
            elif typ == "MESSAGE":
                if data == "ALL":
                    for uid in range(n):
                        ans[uid] += 1
                elif data == "HERE":
                    for uid in range(n):
                        if off[uid] <= ts:
                            ans[uid] += 1
                else:
                    for uid in map(lambda x: int(x[2:]), data.split()):
                        ans[uid] += 1
        return ans
    
sol = Solution()
print(sol.countMentions(2, [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","71","HERE"]])) # [2,2]  
print(sol.countMentions(2, [["MESSAGE","10","id1 id0"],["OFFLINE","11","0"],["MESSAGE","12","ALL"]])) # [2,2]
print(sol.countMentions(2, [["OFFLINE","10","0"],["MESSAGE","12","HERE"]])) # [0,1]
print(sol.countMentions(3, [["MESSAGE","2","HERE"],["OFFLINE","2","1"],["OFFLINE","1","0"],["MESSAGE","61","HERE"]])) # [1,0,2]