# @algorithm @lc id=347 lang=python3 
# @title top-k-frequent-elements


from en.Python3.mod.preImport import *
# @test([1,1,1,2,2,3],2)=[1,2]
# @test([1],1)=[1]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        hp = []
        for key, val in cnt.items():
            heapq.heappush(hp, (val, key))
            if len(hp) > k:
                heapq.heappop(hp)
        ans = []
        while hp:
            ans.append(heapq.heappop(hp)[1])
        return ans