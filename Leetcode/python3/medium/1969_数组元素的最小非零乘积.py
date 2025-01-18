#
# @lc app=leetcode.cn id=1969 lang=python3
#
# [1969] 数组元素的最小非零乘积
#

# @lc code=start
class Solution:
    """
        Greedy + Math + Constructive

        分成 2^{p-1}-1 組，每組有 2 個數字，每組的乘積為 2^p-2，剩下的一個數字為 2^p-1
        (2^p-1) * (2^p-2)^(2^{p-1}-1)
        https://leetcode.cn/problems/minimum-non-zero-product-of-the-array-elements/solutions/936621/tan-xin-ji-qi-shu-xue-zheng-ming-by-endl-uumv/?envType=daily-question&envId=2024-03-20
    """
    def minNonZeroProduct(self, p: int) -> int:
        MOD = 10**9 + 7
        t = pow(2, p) - 1
        return pow(t-1, t//2, MOD) * t % MOD
# @lc code=end

