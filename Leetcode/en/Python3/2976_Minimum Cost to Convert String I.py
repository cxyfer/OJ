# @algorithm @lc id=3235 lang=python3 
# @title minimum-cost-to-convert-string-i


from en.Python3.mod.preImport import *
# @test("abcd","acbe",["a","b","c","c","e","d"],["b","c","b","e","b","e"],[2,5,5,1,2,20])=28
# @test("aaaa","bbbb",["a","c"],["c","b"],[1,2])=12
# @test("abcd","abce",["a"],["e"],[10000])=-1
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        g = [[float("inf")] * 26 for _ in range(26)]
        for i in range(26):
            g[i][i] = 0
        for u, v, w in zip(original, changed, cost):
            uu, vv = ord(u)-ord('a'), ord(v)-ord('a')
            g[uu][vv] = min(g[uu][vv], w) # 這裡要注意，因為可能有重複的邊，所以要取最小值
        # Floyd-Warshall
        for k in range(26):
            for i in range(26):
                if g[i][k] == float("inf"): continue # 不可能由 g[i][k] 轉移到其他點
                for j in range(26):
                    g[i][j] = min(g[i][j], g[i][k]+g[k][j])
        
        ans = 0
        for u, v in zip(source, target):
            uu, vv = ord(u)-ord('a'), ord(v)-ord('a')
            if g[uu][vv] == float("inf"): # 不連通，不可能修改成 target
                return -1
            ans += g[uu][vv]
        return ans