from typing import List
from collections import *

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        def diffTime(t1, t2):
            h1, m1 = int(t1[:2]), int(t1[2:])
            h2, m2 = int(t2[:2]), int(t2[2:])
            return (h2-h1)*60 + (m2-m1)

        cnt = defaultdict(list)
        for name, time in access_times:
            cnt[name].append(time)
        ans = []
        for name, times in cnt.items():
            times.sort()
            n = len(times)
            left = 0
            for idx, time in enumerate(times):
                while diffTime(times[left], time) >= 60:
                    left += 1
                if idx-left+1 >= 3:
                    ans.append(name)
                    break
        ans.sort()
        return ans
sol = Solution()
# ["a"]
print(sol.findHighAccessEmployees([["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]])) 
#Output: ["c","d"]
print(sol.findHighAccessEmployees([["d","0002"],["c","0808"],["c","0829"],["e","0215"],["d","1508"],["d","1444"],["d","1410"],["c","0809"]])) # ["c","d"]
#["ab","cd"]
print(sol.findHighAccessEmployees([["cd","1025"],["ab","1025"],["cd","1046"],["cd","1055"],["ab","1124"],["ab","1120"]])) # ["ab","cd"]

access_times = [["wjmqm","0442"],["wjmqm","0504"],["r","0525"],["va","0436"],["r","0440"],["va","0505"],["va","0509"],["r","0515"],["r","0414"]]
print(sol.findHighAccessEmployees(access_times)) # ["va","r"]