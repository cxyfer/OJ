# @algorithm @lc id=313 lang=python3 
# @title super-ugly-number


from en.Python3.mod.preImport import *
# @test(12,[2,7,13,19])=32
# @test(1,[2,3,5])=1
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