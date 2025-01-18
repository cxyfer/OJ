import math
from typing import *
from collections import *
from functools import lru_cache, cache
from heapq import *
from bisect import *
from itertools import *
import time

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        # 這裡的建圖方法其實不是很好，對於不存在的路徑，建成 float("inf") ，後續 Floyd-Warshall 很容易會 TLE
        g = defaultdict(lambda: defaultdict(lambda: float("inf")))
        len_to_nodes = defaultdict(set) # 不同長度的字串在不同的連通塊中
        for u, v, w in zip(original, changed, cost):
            g[u][v] = min(g[u][v], w)
            len_to_nodes[len(u)].add(u)
            len_to_nodes[len(v)].add(v)
        for l in len_to_nodes:
            for node in len_to_nodes[l]:
                g[node][node] = 0
        # Floyd-Warshall
        for nodes in len_to_nodes.values(): # 不同長度的字串在不同的連通塊中，所以可以分開處理
            for k in nodes:
                for i in nodes:
                    if g[i][k] == float("inf"): # 不可能由 g[i][k] 轉移到其他點
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
            for j in range(max(0, i-max_len), i): # 長度
                node_len = i - j
                u = source[j:i]
                if u not in len_to_nodes[node_len]:
                    continue
                v = target[j:i]
                if v not in len_to_nodes[node_len]:
                    continue
                dp[i] = min(dp[i], dp[j]+g[u][v])
        return dp[n] if dp[n] != float("inf") else -1

sol = Solution()
print(sol.minimumCost(source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20])) # 28
print(sol.minimumCost(source = "abcdefgh", target = "acdeeghh", original = ["bcd","fgh","thh"], changed = ["cde","thh","ghh"], cost = [1,3,5])) # 9 
print(sol.minimumCost(source = "abcd", target = "cdef", original = ["a","b"], changed = ["c","d"], cost = [1,2])) # -1 

t_st = time.time()
source = "hmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqg"
target = "irgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptx"
original = ["hmlns","ydwgtrxofpi","jdqghmln","sydwgtrxofp","ijdqghm","lnsydwg","trxofpijdqg","hmlnsyd","wgtrxofpij","dqghmlns","ydwg","trxofpi","jdqghmlns","ydwgtrxofp","ijdqghmlnsy","dwg","trx","ofpij","dqg","hmln","sydwgtrxo","fpi","jdqghmlnsy","dwg","trxofpij","dqgh","mlnsyd","wgt","rxofpijd","qghmlns","ydwgtrxof","pijdqgh","mlnsy","dwgtrxo","fpijdqg","hml","nsydw","gtr","xofp","ij","dq","ghmlns","ydwgtrxofpi","jdq","ghmlnsydwgtr","xofpij","dqghmln","sy","dwgtrx","ofpijdq","ghml","nsydw","gtrx","ofpij","dqghml","nsydwg","trxofpi","jdqghmlnsyd","wgtrxo","fp","ijdqghmlnsyd","wgtrxo","fpij","dqghmlnsy","dwgtrxo","fpijdqgh","mlnsy","dwgtrxo","fpij","dqg","hmlnsydw","gtrxofpi","jdqghmlnsydw","gtrxofpijd","qghmlnsydw","gtrx","ofpijdq","ghmlnsydw","gtrx","ofpi","jdqg","hmlnsydwgt","rxofp","ijdqg","hmlnsyd","wgtrxofp","ijdqghmlns","ydwgt","rxofp","ijd","qghmln","sy","dwgtr","xofpi","jdqghm","ln","sydw","gtrxofpijd","qghmlnsyd","hmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqghmlnsydwgtrxofpijdqg"]
changed = ["irgki","suzsfywbtsc","rptxirgk","isuzsfywbts","crptxir","gkisuzs","fywbtscrptx","irgkisu","zsfywbtscr","ptxirgki","suzs","fywbtsc","rptxirgki","suzsfywbts","crptxirgkis","uzs","fyw","btscr","ptx","irgk","isuzsfywb","tsc","rptxirgkis","uzs","fywbtscr","ptxi","rgkisu","zsf","ywbtscrp","txirgki","suzsfywbt","scrptxi","rgkis","uzsfywb","tscrptx","irg","kisuz","sfy","wbts","cr","pt","xirgki","suzsfywbtsc","rpt","xirgkisuzsfy","wbtscr","ptxirgk","is","uzsfyw","btscrpt","xirg","kisuz","sfyw","btscr","ptxirg","kisuzs","fywbtsc","rptxirgkisu","zsfywb","ts","crptxirgkisu","zsfywb","tscr","ptxirgkis","uzsfywb","tscrptxi","rgkis","uzsfywb","tscr","ptx","irgkisuz","sfywbtsc","rptxirgkisuz","sfywbtscrp","txirgkisuz","sfyw","btscrpt","xirgkisuz","sfyw","btsc","rptx","irgkisuzsf","ywbts","crptx","irgkisu","zsfywbts","crptxirgki","suzsf","ywbts","crp","txirgk","is","uzsfy","wbtsc","rptxir","gk","isuz","sfywbtscrp","txirgkisu","irgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptxirgkisuzsfywbtscrptx"]
cost = [500,699,75,496,960,551,592,199,484,490,598,521,385,644,605,71,156,58,862,328,99,779,817,236,561,706,828,470,910,471,283,119,750,502,141,277,802,273,671,450,965,375,121,409,779,857,728,883,483,4,641,802,566,263,132,963,162,74,806,559,293,960,475,313,602,132,653,291,486,474,615,269,300,898,419,2,95,149,893,880,249,330,524,674,101,273,152,917,903,25,700,284,413,420,652,659,665,125,574,96345]
print(sol.minimumCost(source, target, original, changed, cost)) 
t_ed = time.time()
print(t_ed - t_st)