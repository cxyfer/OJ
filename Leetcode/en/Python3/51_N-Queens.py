# @algorithm @lc id=51 lang=python3 
# @title n-queens


from en.Python3.mod.preImport import *
# @test(4)=[[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# @test(1)=[["Q"]]
class Solution:
    """
        Backtrace, similar to 46.Permutations.
        直接套模板，額外再檢查對角線即可
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        col = [0] * n # col[i] = j 表示i-th row的皇后在j-th col

        def check(x, y):
            for i in range(x): # 檢查前x列
                j = col[i]
                if x+y == i+j or x-y == i-j: # 檢查對角線，在同一條對角線上，x+y=c或x-y=c
                    return False
            return True
        
        def dfs(r: int, avail: set) -> None:
            if r == n:
                ans.append(['.' * c + 'Q' + '.' * (n - 1 - c) for c in col])
                return
            for c in avail:
                if check(r, c):
                    col[r] = c
                    dfs(r + 1, avail-{c})
        dfs(0, set(range(n)))
        return ans
