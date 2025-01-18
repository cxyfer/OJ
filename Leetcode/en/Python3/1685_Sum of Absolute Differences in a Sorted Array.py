# @algorithm @lc id=1787 lang=python3 
# @title sum-of-absolute-differences-in-a-sorted-array


from en.Python3.mod.preImport import *
# @test([2,3,5])=[4,3,5]
# @test([1,4,6,8,10])=[24,15,13,15,21]
class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        # 前綴和
        pre = [0] * n
        for i in range(1, n):
            pre[i] = pre[i-1] + nums[i-1]
        # 後綴和
        suf = [0] * n
        for i in range(n-2, -1, -1):
            suf[i] = suf[i+1] + nums[i+1]
        # 計算答案
        for i in range(n):
            p = nums[i] * i - pre[i]
            s = suf[i] - nums[i] * (n-i-1)
            ans[i] = p + s
        return ans