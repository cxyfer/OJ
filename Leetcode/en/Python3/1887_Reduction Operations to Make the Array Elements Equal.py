# @algorithm @lc id=2016 lang=python3 
# @title reduction-operations-to-make-the-array-elements-equal


from en.Python3.mod.preImport import *
# @test([5,1,3])=3
# @test([1,1,1])=0
# @test([1,1,2,2,3])=4
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        # 統計比自己小的數字有幾種
        keys = sorted(cnt.keys())
        pre = []
        for key in keys:
            pre.append((pre[-1]+1 if pre else 0))
        ans = 0
        for i, k in enumerate(keys):
            ans += cnt[k] * pre[i]
        return ans