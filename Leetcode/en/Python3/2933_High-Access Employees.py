# @algorithm @lc id=3202 lang=python3 
# @title high-access-employees


from en.Python3.mod.preImport import *
# @test([["a","0549"],["b","0457"],["a","0532"],["a","0621"],["b","0540"]])=["a"]
# @test([["d","0002"],["c","0808"],["c","0829"],["e","0215"],["d","1508"],["d","1444"],["d","1410"],["c","0809"]])=["c","d"]
# @test([["cd","1025"],["ab","1025"],["cd","1046"],["cd","1055"],["ab","1124"],["ab","1120"]])=["ab","cd"]
class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        cnt = defaultdict(list)

        for name, t in access_times:
            time = int(t[:2]) * 60  + int(t[2:])
            cnt[name].append(time)

        ans = []
        for name, times in cnt.items():
            times.sort()
            n = len(times)
            left = 0
            for idx, time in enumerate(times):
                while time - times[left] >= 60:
                    left += 1
                if idx-left+1 >= 3:
                    ans.append(name)
                    break
        ans.sort()
        return ans