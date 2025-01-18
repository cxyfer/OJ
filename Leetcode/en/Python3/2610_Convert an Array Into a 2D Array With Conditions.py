# @algorithm @lc id=2724 lang=python3 
# @title convert-an-array-into-a-2d-array-with-conditions


from en.Python3.mod.preImport import *
# @test([1,3,4,1,2,3,1])=[[1,3,4,2],[1,3],[1]]
# @test([1,2,3,4])=[[4,3,2,1]]
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        ans = defaultdict(list)
        cnt = Counter(nums)
        for k, v in cnt.items():
            for i in range(v):
                ans[i].append(k)
        return list(ans.values())