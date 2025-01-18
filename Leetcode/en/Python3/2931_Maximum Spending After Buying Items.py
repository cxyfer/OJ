# @algorithm @lc id=3107 lang=python3 
# @title maximum-spending-after-buying-items


from en.Python3.mod.preImport import *
# @test([[8,5,2],[6,4,1],[9,7,3]])=285
# @test([[10,8,6,4,2],[9,7,5,3,2]])=386
class Solution:
    """
        Min Heap
    """
    def maxSpending(self, values: List[List[int]]) -> int:
        m, n = len(values), len(values[0])
        ans = 0
        last = [n-1 for i in range(m)]
        hp = [(values[i][-1], i) for i in range(m)]
        heapq.heapify(hp)
        for d in range(1, m*n+1):
            val, idx = heapq.heappop(hp)
            ans += val * d
            if last[idx] > 0: # 這個idx還有東西可以買
                heapq.heappush(hp, (values[idx][last[idx]-1], idx))
                last[idx] -= 1
        return ans