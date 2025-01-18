# @algorithm @lc id=3238 lang=python3 
# @title minimum-cost-to-convert-string-ii


from en.Python3.mod.preImport import *
# @test("abcd","acbe",["a","b","c","c","e","d"],["b","c","b","e","b","e"],[2,5,5,1,2,20])=28
# @test("abcdefgh","acdeeghh",["bcd","fgh","thh"],["cde","thh","ghh"],[1,3,5])=9
# @test("abcdefgh","addddddd",["bcd","defgh"],["ddd","ddddd"],[100,1578])=-1
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # 這裡的建圖方法其實不是很好，對於不存在的路徑，建成 float("inf") ，後續 Floyd-Warshall 很容易會 TLE
        g = defaultdict(lambda: defaultdict(lambda: float("inf")))
        len_to_nodes = defaultdict(set) # 不同長度的字串在不同的連通塊中
        for u, v, w in zip(original, changed, cost):
            g[u][v] = min(g[u][v], w)
            len_to_nodes[len(u)].add(u)
            len_to_nodes[len(v)].add(v)
            g[u][u] = 0
            g[v][v] = 0
        # Floyd-Warshall
        for nodes in len_to_nodes.values(): # 不同長度的字串在不同的連通塊中，所以可以分開處理
            for k in nodes:
                for i in nodes:
                    if g[i][k] == float("inf"): # 不可能由 g[i][k] 轉移到其他點，巨大優化
                        continue
                    for j in nodes:
                        g[i][j] = min(g[i][j], g[i][k]+g[k][j])
        max_len = max(len_to_nodes.keys())
        # dp[i] 表示 修改 source[:i] 為 target[:i] 的最小代價
        n = len(source)
        dp = [float("inf")] * (n+1)
        dp[0] = 0
        for i in range(1, n+1):
            if source[i-1] == target[i-1]: # 可以選擇不修改
                dp[i] = dp[i-1]
            # 1. 枚舉轉移起始點 j
            # for j in range(max(0, i-max_len), i): 
            #     size = i - j
            #     if size not in len_to_nodes: # 不加會 TLE ，測資中可能有很多不存在於[0, max_len] 之間的長度
            #         continue
            #     nodes = len_to_nodes[size]
            # 2. 枚舉轉移部份的長度 size ，比枚舉 j 快很多
            for size, nodes in len_to_nodes.items(): 
                if i < size:
                    continue
                j = i-size
                # 取出 source[j:i] 與 target[j:i] ，並判斷是否存在於 g 中
                u = source[j:i]
                v = target[j:i]
                if v in nodes and u in nodes:
                    dp[i] = min(dp[i], dp[j]+g[u][v])
        return dp[n] if dp[n] != float("inf") else -1