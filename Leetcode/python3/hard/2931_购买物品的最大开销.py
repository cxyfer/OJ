#
# @lc app=leetcode.cn id=2931 lang=python3
#
# [2931] 购买物品的最大开销
#
from preImport import *
# @lc code=start
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
# @lc code=end

