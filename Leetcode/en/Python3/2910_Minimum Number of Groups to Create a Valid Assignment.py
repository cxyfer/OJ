# @algorithm @lc id=3166 lang=python3 
# @title minimum-number-of-groups-to-create-a-valid-assignment

from en.Python3.mod.preImport import *
# @test([3,2,3,2,3])=2
# @test([10,10,10,3,1,1])=4
# @test([2,3,2,1,3,1,1,2,3,1,1])=4
class Solution:
    def minGroupsForValidAssignment(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        for k in range(min(cnt.values()), 0, -1): # k 為每個組的元素數量
            ans = 0
            for v in cnt.values():
                q1, r1 = divmod(v, k)
                if q1 < r1:
                    break
                ans += (v+k) // (k+1)
            else:
                return ans
