#
# @lc app=leetcode id=1742 lang=python3
# @lcpr version=30204
#
# [1742] Maximum Number of Balls in a Box
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
"""
1. Brute Force
2. Digit DP
"""
# @lc code=start
class Solution1:
    def countBalls(self, lo: int, hi: int) -> int:
        cnt = defaultdict(int)
        def digit_sum(x: int) -> int:
            res = 0
            while x:
                res += x % 10
                x //= 10
            return res
        for x in range(lo, hi + 1):
            cnt[digit_sum(x)] += 1
        return max(cnt.values())
    
class Solution2:
    def countBalls(self, l: int, r: int) -> int:
        low = list(map(int, str(l)))
        high = list(map(int, str(r)))
        n = len(high)
        diff = n - len(low)
        low = [0] * (n - len(low)) + low  # 補前導零，使 low 和 high 對齊

        @cache
        def dfs(i: int, j: int, limit_low: bool, limit_high: bool) -> int:
            if i == n:
                return j == 0

            # 第 i 個數位可以從 lo 枚舉到 hi
            # 如果對數位還有其它約束，應該只在下面的 for 迴圈做限制，不應修改 lo 或 hi
            lo = low[i] if limit_low else 0
            hi = high[i] if limit_high else 9

            res = 0
            for d in range(lo, min(hi, j) + 1):
                res += dfs(i + 1, j - d, limit_low and d == lo, limit_high and d == hi)
            return res

        mx = 9 * n
        return max(dfs(0, i, True, True) for i in range(1, mx + 1))

# Solution = Solution1
Solution = Solution2
# @lc code=end

sol = Solution()
print(sol.countBalls(1, 10))  # 2
print(sol.countBalls(5, 15))  # 2
print(sol.countBalls(19, 28))  # 2

#
# @lcpr case=start
# 1\n10\n
# @lcpr case=end

# @lcpr case=start
# 5\n15\n
# @lcpr case=end

# @lcpr case=start
# 19\n28\n
# @lcpr case=end

#

