# You are given a 0-indexed m * n integer matrix values, representing the values of m * n different items in m different shops. Each shop has n items where the jth item in the ith shop has a value of values[i][j]. Additionally, the items in the ith shop are sorted in non-increasing order of value. That is, values[i][j] >= values[i][j + 1] for all 0 <= j < n - 1.

# On each day, you would like to buy a single item from one of the shops. Specifically, On the dth day you can:

# Pick any shop i.
# Buy the rightmost available item j for the price of values[i][j] * d. That is, find the greatest index j such that item j was never bought before, and buy it for the price of values[i][j] * d.
# Note that all items are pairwise different. For example, if you have bought item 0 from shop 1, you can still buy item 0 from any other shop.

# Return the maximum amount of money that can be spent on buying all m * n products.

from typing import List
import heapq

class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        m, n = len(values), len(values[0])
        ans = 0
        last = [n-1 for i in range(m)]
        hp = [(values[i][-1], i) for i in range(m)]
        heapq.heapify(hp)
        for d in range(1, m*n+1):
            v, idx = heapq.heappop(hp)
            ans += v * d
            if last[idx] > 0:
                heapq.heappush(hp, (values[idx][last[idx]-1], idx))
                last[idx] -= 1
        return ans
sol = Solution()
print(sol.maxSpending([[8,5,2],[6,4,1],[9,7,3]])) # 285
print(sol.maxSpending([[10,8,6,4,2],[9,7,5,3,2]])) # 386
        