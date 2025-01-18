#
# @lc app=leetcode id=3139 lang=python3
#
# [3139] Minimum Cost to Equalize Array
#
from preImport import *
# @lc code=start
class Solution:
    """
        相等後的數不一定是最大值
    """
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        mx, mn = max(nums), min(nums)
        base = mx * n - sum(nums)
        if n <= 2 or cost2 >= 2 * cost1: # 用 cost1 就好
            return base * cost1 % MOD # 除了最大值以外的都變成最大值

        def f(x: int) -> int:
            s = base + (x - mx) * n # 需要增加的數字總和
            d = x - mn # 最大的差
            if d * 2 <= s: # 最大的差沒有超過總和的一半，可以用操作2一起操作 (若 s 為偶數)
                return s // 2 * cost2 + s % 2 * cost1
            return (s - d) * cost2 + (d * 2 - s) * cost1

        ans = float("inf")
        for x in range(mx, mx * 2 +1):
            res = f(x)
            if res < ans:
                ans = res
        return ans % MOD
# @lc code=end
sol = Solution()
print(sol.minCostToEqualizeArray([4,1], 5, 2)) # 15
print(sol.minCostToEqualizeArray([2,3,3,3,5], 2, 1)) # 6
print(sol.minCostToEqualizeArray([3,5,3], 1, 3)) # 4
print(sol.minCostToEqualizeArray([1,14,14,15], 2, 1)) # 20
print(sol.minCostToEqualizeArray([4,3], 2, 6)) # 2
print(sol.minCostToEqualizeArray([4,3,1,8], 5, 1)) # 8


print(sol.minCostToEqualizeArray([1,1000000,999999], 1000000, 1)) # 1999997