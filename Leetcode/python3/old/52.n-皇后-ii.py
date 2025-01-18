#
# @lc app=leetcode.cn id=52 lang=python3
#
# [52] N 皇后 II
#

# @lc code=start
class Solution:
    """
        Backtrace, similar to 46.Permutations.
        直接套模板，額外再檢查對角線即可，把51題的答案取len即可
    """
    def totalNQueens(self, n: int) -> int:
        ans = 0
        col = [0] * n # col[i] = j 表示i-th row的皇后在j-th col

        def check(x, y):
            for i in range(x): # 檢查前x列
                j = col[i]
                if x+y == i+j or x-y == i-j: # 檢查對角線，在同一條對角線上，x+y=c或x-y=c
                    return False
            return True
        
        def dfs(r: int, avail: set) -> None:
            nonlocal ans
            if r == n:
                ans += 1
                return
            for c in avail:
                if check(r, c):
                    col[r] = c
                    dfs(r + 1, avail-{c})
        dfs(0, set(range(n)))
        return ans
# @lc code=end
sol = Solution()
for i in range(1, 10):
    print(sol.totalNQueens(i))

