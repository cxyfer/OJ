# @algorithm @lc id=1364 lang=python3 
# @title tuple-with-same-product


from en.Python3.mod.preImport import *
# @test([2,3,4,6])=8
# @test([1,2,4,5,10])=16
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = Counter()
        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                product = nums[i] * nums[j]
                cnt[product] += 1
                if cnt[product] > 1:
                    ans += (cnt[product] - 1) * 8
        return ans