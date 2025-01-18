#
# @lc app=leetcode.cn id=313 lang=python3
#
# [313] 超级丑数
#
from preImport import *
# @lc code=start
class Solution:
    """
        Heap
    """
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        visited = set()
        hp = [1]
        heapq.heapify(hp)
        for _ in range(n):
            ugly = heapq.heappop(hp)
            for factor in primes:
                new_ugly = ugly * factor
                if new_ugly not in visited:
                    visited.add(new_ugly)
                    heapq.heappush(hp, new_ugly)
        return ugly
# @lc code=end

