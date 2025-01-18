# @algorithm @lc id=3176 lang=python3 
# @title minimum-sum-of-mountain-triplets-i


from en.Python3.mod.preImport import *
# @test([8,6,1,5,3])=9
# @test([5,4,8,7,10,2])=13
# @test([6,5,4,3,4,5])=-1
class Solution:
    """
        prefix and suffix minimum
    """
    def minimumSum(self, nums: List[int]) -> int:
        
        n = len(nums)
        pre, suf = [float('inf') for _ in range(n)], [float('inf') for _ in range(n)]
        pre[0] = nums[0]
        suf[-1] = nums[-1]
        for i in range(1, n):
            pre[i] = min(pre[i-1], nums[i])
        for i in range(n-2, -1, -1):
            suf[i] = min(suf[i+1], nums[i])
        print(pre)
        print(suf)
        ans = float('inf')
        for i in range(1, n-1):
            if pre[i-1] < nums[i] and nums[i] > suf[i+1]:
                ans = min(ans, pre[i-1] + nums[i] + suf[i+1])
        return ans if ans != float('inf') else -1


