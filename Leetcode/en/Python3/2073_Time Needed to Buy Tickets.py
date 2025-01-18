# @algorithm @lc id=2195 lang=python3 
# @title time-needed-to-buy-tickets


from en.Python3.mod.preImport import *
# @test([2,3,2],2)=6
# @test([5,1,1,1],0)=8
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        target = tickets[k]
        res1 = sum([min(target, t) for t in tickets[:k]])
        res2 = sum([min(target-1, t) for t in tickets[k+1:]])
        return res1 + target + res2