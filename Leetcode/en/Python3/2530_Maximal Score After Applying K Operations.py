# @algorithm @lc id=2616 lang=python3 
# @title maximal-score-after-applying-k-operations


from en.Python3.mod.preImport import *
# @test([10,10,10,10,10],5)=50
# @test([1,10,3,3,3],3)=17
class Solution:
    """
        Greedy + Heap
    """
    def maxKelements(self, nums: List[int], k: int) -> int:
        ans = 0
        h = []
        for num in nums:
            heapq.heappush(h, -num)
        for _ in range(k):
            res = -heapq.heappop(h)
            ans += res
            heapq.heappush(h, -ceil(res/3))
        return ans