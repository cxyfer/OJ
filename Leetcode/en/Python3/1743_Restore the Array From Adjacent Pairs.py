# @algorithm @lc id=1866 lang=python3 
# @title restore-the-array-from-adjacent-pairs


from en.Python3.mod.preImport import *
# @test([[2,1],[3,4],[3,2]])=[1,2,3,4]
# @test([[4,-2],[1,4],[-3,1]])=[-2,4,1,-3]
# @test([[100000,-100000]])=[100000,-100000]
class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        n = len(adjacentPairs) + 1
        tbl = defaultdict(list)
        for x, y in adjacentPairs:
            tbl[x].append(y)
            tbl[y].append(x)
        st = -1
        for k, v in tbl.items():
            if len(v) == 1:
                st = k
                break
        ans = [0] * n
        ans[0] = st
        ans[1] = tbl[st][0]
        for i in range(2, n):
            for x in tbl[ans[i-1]]:
                if x != ans[i-2]:
                    ans[i] = x
                    break
        return ans