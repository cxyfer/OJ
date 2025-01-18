# @algorithm @lc id=60 lang=python3 
# @title permutation-sequence


from en.Python3.mod.preImport import *
# @test(3,3)="213"
# @test(4,9)="2314"
# @test(3,1)="123"
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        fact = [1]
        for i in range(1, 10):
            fact.append(fact[-1] * i)

        visited = [False for _ in range(n + 1)]
        path = []

        def dfs(i):
            nonlocal k
            if i == n:
                return
            cnt = fact[n - 1 - i] # (n-1)!
            for j in range(1, n + 1):
                if visited[j]: # 已經用過
                    continue
                if cnt < k: # 比j開頭的排列數還多，考慮下一個數字
                    k -= cnt
                    continue
                path.append(j) # 這個位置是j
                visited[j] = True
                dfs(i + 1)
                return
        dfs(0)
        return ''.join(map(str, path))