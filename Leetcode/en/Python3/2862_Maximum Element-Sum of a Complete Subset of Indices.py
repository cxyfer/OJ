# @algorithm @lc id=3047 lang=python3 
# @title maximum-element-sum-of-a-complete-subset-of-indices


from en.Python3.mod.preImport import *
# @test([8,7,3,5,7,2,4,9])=16
# @test([5,10,3,10,1,13,7,9,4])=19
class Solution:
    """
        枚舉core()為i的下標
        好像懂了又好像沒懂
    """
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(1, n + 1):
            s = 0
            for j in range(1, isqrt(n // i) + 1):
                s += nums[i * j * j - 1]  # -1 是因为数组下标从 0 开始
            ans = max(ans, s)
        return ans