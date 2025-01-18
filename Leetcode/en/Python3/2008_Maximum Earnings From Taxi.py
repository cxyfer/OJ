# @algorithm @lc id=2118 lang=python3 
# @title maximum-earnings-from-taxi


from en.Python3.mod.preImport import *
# @test(5,[[2,5,4],[1,5,1]])=7
# @test(20,[[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]])=20
class Solution:
    """
        DP + Binary Search
        本質上就是 Weighted Interval Scheduling 問題
        https://www.csie.ntu.edu.tw/~yvchen/f111-ada/
        dp[i]表示只接受前i個乘客的最大收益，對於第i個乘客，我們可以選擇接或不接
        若接的話則需要考慮上一個乘客是誰，
    """
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        m = len(rides)
        rides.sort(key=lambda x: x[1])
        dp = [0] * (m + 1)
        for i, (st, ed, tip) in enumerate(rides):
            w = ed - st + tip # weight
            j = bisect_right(rides, st, hi=i, key=lambda x: x[1])
            dp[i + 1] = max(dp[i], dp[j] + w)
        return dp[m]
