#
# @lc app=leetcode id=2712 lang=python3
#
# [2712] Minimum Cost to Make All Characters Equal
#


# @lcpr-template-start
from preImport import *
# @lcpr-template-end
# @lc code=start
class Solution1:
    def minimumCost(self, s: str) -> int:
        # return sum(min(i + 1, len(s) - i - 1) for i, (x, y) in enumerate(pairwise(s)) if x != y)
        n = len(s)
        ans = 0
        for i, (x, y) in enumerate(pairwise(s)):
            if x != y:
                ans += min(i + 1, n - i - 1)
        return ans
    
class Solution2a:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        lst = list(map(int, s))
        # pre(i, j) 表示只透過操作1，將 s[:i+1] 變成 j 的最小成本
        @cache
        def pre(i: int, j: int) -> int:
            if i == -1:
                return 0
            return pre(i - 1, lst[i]) + (lst[i] != j) * (i + 1)
        # suf(i, j) 表示只透過操作2，將 s[i:] 變成 j 的最小成本
        @cache
        def suf(i: int, j: int) -> int:
            if i == n:
                return 0
            return suf(i + 1, lst[i]) + (lst[i] != j) * (n - i)
        return min(pre(i, x) + suf(i + 1, x) for i in range(n) for x in range(2))
    
class Solution2b:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        lst = list(map(int, s))
        # suf[i][j] 表示只透過操作2，將 s[i:] 變成 j 的最小成本
        suf = [[float('inf')] * 2 for _ in range(n)] + [[0, 0]]
        for i in range(n - 1, -1, -1):
            x = lst[i]
            for j in range(2):
                suf[i][j] = suf[i + 1][x] + (x != j) * (n - i)
        ans = float('inf')
        pre = [0, 0]
        for i, x in enumerate(lst):
            for j in range(2):
                pre[j] = pre[x] + (x != j) * (i + 1)
                ans = min(ans, pre[j] + suf[i + 1][j])
        return ans

Solution = Solution1
# Solution = Solution2a
# Solution = Solution2b
# @lc code=end

sol = Solution()
print(sol.minimumCost("0011"))  # 2
print(sol.minimumCost("010101"))  # 9
