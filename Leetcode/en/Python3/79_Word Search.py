# @algorithm @lc id=79 lang=python3 
# @title word-search


from en.Python3.mod.preImport import *
# @test([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCCED")=true
# @test([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"SEE")=true
# @test([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]],"ABCB")=false
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(i, x, y):
            if i == len(word) - 1:
                return True if board[x][y] == word[i] else False
            if board[x][y] != word[i]:
                return False
            board[x][y] = ''
            for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] != '':
                    if dfs(i+1, nx, ny):
                        return True
            board[x][y] = word[i]
            return False

        for i in range(m):
            for j in range(n):
                if dfs(0, i, j):
                    return True
        return False