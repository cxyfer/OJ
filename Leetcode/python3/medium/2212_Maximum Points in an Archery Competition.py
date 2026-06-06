#
# @lc app=leetcode id=2212 lang=python3
#
# [2212] Maximum Points in an Archery Competition
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. Knapsack DP + Backtracking
2. 二進位枚舉
"""
# @lc code=start
max = lambda a, b: a if a > b else b


class Solution1:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        n = len(aliceArrows)

        f = [[0] * (numArrows + 1) for _ in range(n + 1)]
        for i, a in enumerate(aliceArrows):
            v = i
            w = a + 1
            for j in range(numArrows + 1):
                # 這裡的分支寫法相比於一律先複製 f[i + 1][j] = f[i][j] 再比較大小的寫法，可以帶來不錯的常數優化
                if j >= w:
                    f[i + 1][j] = max(f[i][j], f[i][j - w] + v)
                else:
                    f[i + 1][j] = f[i][j]

        ans = [0] * n
        rem = numArrows
        for i in range(n - 1, -1, -1):
            v = i
            w = aliceArrows[v] + 1
            if rem >= w and f[i + 1][rem] == f[i][rem - w] + v:
                ans[i] = w
                rem -= w
        ans[0] += rem
        return ans


class Solution2:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        n = len(aliceArrows)

        ans = [0] * n
        mx = 0
        for msk in range(1 << n):
            cur = 0
            rem = numArrows
            for i, a in enumerate(aliceArrows):
                if (msk >> i) & 1:
                    cur += i
                    rem -= a + 1
            if rem >= 0 and cur > mx:
                mx = cur
                for i, a in enumerate(aliceArrows):
                    ans[i] = a + 1 if (msk >> i) & 1 else 0
                ans[0] += rem
        return ans


Solution = Solution1
# Solution = Solution2
# @lc code=end

