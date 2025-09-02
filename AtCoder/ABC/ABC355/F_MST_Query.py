"""
    Reference:
     - https://atcoder.jp/contests/abc355/submissions/53921579
"""
from atcoder.dsu import DSU

N, Q = map(int, input().split())
queries = [list(map(int, input().split())) for _ in range(N-1+Q)]

g = [DSU(N+1) for _ in range(10)] # 不同權種下的 DSU
ans = 10 * (N - 1) # 假設 N - 1 條邊的權重都是 10

for i, (u, v, w) in enumerate(queries):
    for j in range(w, 10): # 從權重 w 開始合併
        if g[j].same(u, v):
            continue
        g[j].merge(u, v)
        ans -= 1 # 每合併一次，答案就減一
    if i >= N-1:
        print(ans)