"""
    先在不使用 Xpress 的情況下，分別從起點和終點跑 Dijkstra，
    由於只能使用 Xpress 一次，所以可以枚舉經過 Xpress 的邊 (u, v, w)，看是否會比原本的答案更短。
"""

from heapq import *

kase = 0
while True:
    try:
        if kase > 0:
            input()
            print()
        kase += 1
        n, s, e = map(int, input().split())
    except EOFError:
        break
    m = int(input())
    g = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, w = map(int, input().split())
        g[u].append((v, w))
        g[v].append((u, w))
    k = int(input())
    edges = [] # Xpress
    for _ in range(k):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    
    def dijkstra(s):
        dist = [float('inf')] * (n + 1)
        dist[s] = 0
        path = [[] for _ in range(n + 1)]
        path[s] = [s]
        hp = [(0, s)]
        while hp:
            d, u = heappop(hp)
            if d > dist[u]: continue
            for v, w in g[u]:
                if d + w < dist[v]:
                    dist[v] = d + w
                    path[v] = path[u] + [v]
                    heappush(hp, (dist[v], v))
        return dist, path
    
    dist1, path1 = dijkstra(s) # 從起點開始
    dist2, path2 = dijkstra(e) # 從終點開始
    ans, path, idx = dist1[e], path1[e], -1 # 初始化答案為不使用 Xpress 的情況
    for i, (u, v, w) in enumerate(edges): # 使用 Xpress 在邊 (u, v, w) 上
        if dist1[u] + w + dist2[v] < ans: # 如果 s -> u -> v -> e 比原本的答案更短
            ans = dist1[u] + w + dist2[v]
            path = path1[u] + path2[v][::-1]
            idx = u
        if dist1[v] + w + dist2[u] < ans: # 如果 s -> v -> u -> e 比原本的答案更短
            ans = dist1[v] + w + dist2[u]
            path = path1[v] + path2[u][::-1]
            idx = v
    print(*path)
    print(idx if idx != -1 else 'Ticket Not Used')
    print(ans)