# @algorithm @lc id=264 lang=python3 
# @title ugly-number-ii


from en.Python3.mod.preImport import *
# @test(10)=12
# @test(1)=1
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # return self.solveByMerge3SortedLists(n)
        return self.solveByHeap(n)
    """
        1. Merge 3 sorted list
    """
    def solveByMerge3SortedLists(self, n: int) -> int:
        p = p2 = p3 = p5 = 1 # Pointers
        ugly = [0]
        res2 = res3 = res5 = 1
        while p <= n:
            min_ugly = min(res2, res3, res5)
            ugly.append(min_ugly)
            p += 1
            if min_ugly == res2:
                res2 = ugly[p2] * 2
                p2 += 1
            elif min_ugly == res3:
                res3 = ugly[p3] * 3
                p3 += 1
            elif min_ugly == res5:
                res5 = ugly[p5] * 5
                p5 += 1
        return ugly[n]
    """
        2. Heap
    """
    def solveByHeap(self, n: int) -> int:
        visited = set()
        hp = [1]
        heapq.heapify(hp)
        for _ in range(n):
            ugly = heapq.heappop(hp)
            for factor in [2, 3, 5]:
                new_ugly = ugly * factor
                if new_ugly not in visited:
                    visited.add(new_ugly)
                    heapq.heappush(hp, new_ugly)
        return ugly