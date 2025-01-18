"""
    內向基環樹(pseudotree)

    如果一张有向弱连通图每个点的出度都为 1，则称它是一棵 基环内向树。

    Topological Sort

    Same as 2876. Count Visited Nodes in a Directed Graph
"""
from collections import deque

N = int(input())
A = list(map(int, input().split()))

rg = [[] for _ in range(N)] # 反向圖
deg = [0] * N
for x, y in enumerate(A):
    rg[y - 1].append(x) # 建反向圖
    deg[y - 1] += 1

q = deque(i for i, d in enumerate(deg) if d == 0) # 拓撲排序
while q: # 剪掉 基環樹 上的所有樹枝，只留下基環
    x = q.popleft()
    y = A[x] - 1
    deg[y] -= 1
    if deg[y] == 0:
        q.append(y)

ans = [0] * N

def rdfs(x: int, depth: int) -> None:
    ans[x] = depth
    for y in rg[x]:
        if deg[y] == 0: # 樹枝上的點在拓撲排序後，入度均為 0
            rdfs(y, depth + 1)
    
for i, d in enumerate(deg):
    if d <= 0: # 非環上的點，或是已經處理過的環
        continue
    ring = []
    x = i
    while True:
        deg[x] = -1 # 將基環上的點的入度標記為 -1，避免重複訪問
        ring.append(x) # 收集在基環上的點
        x = A[x] - 1
        if x == i: # 訪問完一個環
            break
    for x in ring:
        rdfs(x, len(ring)) # 為方便計算，以 len(ring) 作為初始深度
print(sum(ans))