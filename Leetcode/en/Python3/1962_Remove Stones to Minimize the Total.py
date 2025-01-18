# @algorithm @lc id=2094 lang=python3 
# @title remove-stones-to-minimize-the-total


from en.Python3.mod.preImport import *
# @test([5,4,9],2)=12
# @test([4,3,6,7],3)=12
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        n = len(piles)
        hp = [-x for x in piles]
        heapify(hp)
        for _ in range(k):
            x = -heappop(hp)
            heappush(hp, -(x - x // 2))
        return -sum(hp)