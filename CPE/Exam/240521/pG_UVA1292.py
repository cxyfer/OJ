"""
    UVA 上 Python 需要開輸出入優化，不然在 TLE 邊緣
    AC: UVA, CPE, ZeroJudge
"""
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def print(val=""):
    sys.stdout.write(str(val) + "\n")

while True:
    try:
        n = int(input())
    except:
        break

    g = [[] for _ in range(n)]
    for _ in range(n):
        line = input()
        co, lp, rp = line.index(':'), line.index('('), line.index(')')
        u, d = int(line[:co]), int(line[lp+1:rp])
        nodes = list(map(int, line[rp+2:].split()))
        for v in nodes:
            g[u].append(v)
            g[v].append(u)

    def dfs(u, fa):
        f0, f1 = 0, 1 # 當前節點 不放置/放置 的最小花費
        for v in g[u]:
            if v == fa:
                continue
            r0, r1 = dfs(v, u)
            f0 += r1 # 若不放置，下一層必須放置
            f1 += min(r0, r1) # 若放置，下一層可放置或不放置
        return f0, f1
    print(min(dfs(0, -1))) # 可以以任意點為根