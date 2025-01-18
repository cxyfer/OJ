# @algorithm @lc id=3364 lang=python3 
# @title minimum-sum-of-values-by-dividing-array


from en.Python3.mod.preImport import *
# @test([1,4,3,3,2],[0,3,3,2])=12
# @test([2,3,5,7,7,7,5],[0,7,5])=17
# @test([1,2,3,4],[2])=-1
class Solution:
    """
        劃分型DP
        令 f(i, j, cur) 表示前 i 個數字分成 j 段，且最後一段的 AND值 為 cur 的最小和
        每段初始化為 -1，即二進位全為 1，表示未分段

        https://leetcode.cn/problems/minimum-sum-of-values-by-dividing-array/solutions/2739258/ji-yi-hua-sou-suo-jian-ji-xie-fa-by-endl-728z/
    """
    def minimumValueSum(self, nums: List[int], andValues: List[int]) -> int:
        n, m = len(nums), len(andValues)

        @cache # Memoization
        def f(i: int, j: int, cur: int) -> int:
            if i == n: # 分完了，檢查是否分了 m 段
                return 0 if j == m else float('inf')
            if j == m: # 還沒分完就已經有 m 段了
                return float('inf')
            cur &= nums[i] # AND
            if cur < andValues[j]: # 這段的AND值無法等於 andValues[j]
                return float('inf')
            # 不分段 / 分段
            res = f(i + 1, j, cur) # 不分
            if cur == andValues[j]: # 分
                res = min(res, f(i + 1, j + 1, (1 << 31) - 1) + nums[i])
            return res
        
        ans = f(0, 0, (1 << 31) - 1)
        return ans if ans < float('inf') else -1