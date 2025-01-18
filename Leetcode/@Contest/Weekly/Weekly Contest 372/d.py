from typing import List
from collections import defaultdict

class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        # 找所在位置右邊的第一個比自己高的
        n = len(heights)
        res = defaultdict(list)
        for i in range(n-1):
            for j in range(i+1, n):
                if heights[i] < heights[j]:
                    res[i].append(j)
        # print(heights, res, '', sep='\n')
        ans = []
        for ai, bi in queries:
            if ai > bi: # 保證 ai < bi
                ai, bi = bi, ai
            # print(ai, bi, heights[ai], heights[bi])
            # b柱本身就能當作目標柱
            if heights[bi] > heights[ai] or ai == bi:
                ans.append(bi)
                continue
            # a一定不能當作目標柱(a<b)，且b既不能當作目標柱，右邊也沒有比b更高的柱子
            if not res[ai] or not res[bi]:
                ans.append(-1)
                continue

            # 已經確保目標高樓存在
            t = max(res[ai][0], res[bi][0])
            if heights[t] > heights[ai] and heights[t] > heights[bi]: # 比ab都高
                ans.append(t)
            else: # 只能往右邊找
                flag = False
                for x in res[bi]:
                    if heights[x] > heights[ai] and heights[x] > heights[bi]:
                        ans.append(x)
                        flag = True
                        break
                if not flag:
                    ans.append(-1)
        return ans

sol = Solution()
print(sol.leftmostBuildingQueries([6,4,8,5,2,7], [[0,1],[0,3],[2,4],[3,4],[2,2]])) # [2,5,-1,5,2]
print(sol.leftmostBuildingQueries([5,3,8,2,6,1,4,6], [[0,7],[3,5],[5,2],[3,0],[1,6]])) # [7,6,-1,4,6]

heights = [3,4,1,2]
queries = [[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3],[3,0],[3,1],[3,2],[3,3]]
print(sol.leftmostBuildingQueries(heights, queries)) # [0,1,-1,-1,1,1,-1,-1,-1,-1,2,3,-1,-1,3,3]

print(list([0,1,-1,-1,1,1,-1,-1,-1,-1,2,3,-1,-1,3,3]))
