# @algorithm @lc id=3328 lang=python3 
# @title apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k


from en.Python3.mod.preImport import *
# @test(11)=5
# @test(1)=0
class Solution:
    def minOperations(self, k: int) -> int:
        # return self.solve1(k)
        return self.solve2(k)
    """
        1. Greedy
        為使操作次數最小，顯然應該先對最大的數字進行+1操作，再複製最大的數字
        枚舉最大的數字 m ，需要 m-1 次+1操作，再複製 ((k-1)//m + 1) - 1 次
        TS: O(k)
        SC: O(1)
    """
    def solve1(self, k: int) -> int:
        ans = float("inf")
        for m in range(1, k+1): # 枚舉最大的數字 m
            ans = min(ans, m-1 + (k-1)//m)
        return ans
    """
        2. Math
        f(x) = x + n/x 在 n > 0 的情況下，最小值會發生在 x = sqrt(n)
        由於目標是 x 為整數下的最小值，故取 isqrt
        https://leetcode.cn/problems/apply-operations-to-make-sum-of-array-greater-than-or-equal-to-k/
    """
    def solve2(self, k: int) -> int:
        rt = max(math.isqrt(k-1), 1)
        return min(rt - 1 + (k - 1) // rt, rt + (k - 1) // (rt + 1))
