# @algorithm @lc id=2692 lang=python3 
# @title take-gifts-from-the-richest-pile


from en.Python3.mod.preImport import *
# @test([25,64,9,4,100],4)=29
# @test([1,1,1,1],4)=4
from sortedcontainers import SortedList
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        lst = SortedList(gifts)
        for i in range(k):
            lst.add(isqrt(lst.pop()))
        return sum(lst)