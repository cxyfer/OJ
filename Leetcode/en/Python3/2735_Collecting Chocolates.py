# @algorithm @lc id=2810 lang=python3 
# @title collecting-chocolates


from en.Python3.mod.preImport import *
# @test([20,1,15],5)=13
# @test([1,2,3],4)=6
class Solution:
    def minCost(self, nums: List[int], x: int) -> int:

        n = len(nums)
        ans = [x * i for i in range(n)]
        s = list(range(0, n * x, x))  # s[k] 统计操作 k 次的总成本
        for i, mn in enumerate(nums):  # 子数组左端点
            for j in range(i, n + i):  # 子数组右端点（把数组视作环形的）
                mn = min(mn, nums[j % n])  # 维护从 nums[i] 到 nums[j] 的最小值
                s[j - i] += mn  # 累加操作 j-i 次的花费
        return min(s)

