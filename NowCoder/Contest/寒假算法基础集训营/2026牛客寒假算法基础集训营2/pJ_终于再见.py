"""
J. 终于再见
https://ac.nowcoder.com/acm/contest/120562/J

多源BFS

反向思考，與其從每個點找更高等級的目標，不如以高等級城市做為源點，計算它們到各點的最短距離。
則每次只需要將當前等級的點加入源點，更新到更低等級的點的距離即可。

由於等級的數量最多只有 sqrt(m) 種，因此最多只需要進行 sqrt(m) 次 BFS。
"""
from collections import deque

def solve():
    n, m = map(int, input().split())
    g = [[] for _ in range(n)]
    deg = [0] * n
    for _ in range(m):
        u, v = map(lambda x: int(x) - 1, input().split())
        g[u].append(v)
        g[v].append(u)
        deg[u] += 1
        deg[v] += 1
    
    mp = [[] for _ in range(n)]
    for u, d in enumerate(deg):
        mp[d].append(u)

    ans = [-1] * n
    dist = [float('inf')] * n

    for d in range(n - 1, -1, -1):
        # 此時 dist[u] 存的是比 d 更高等級的點到 u 的最短距離，紀錄答案
        for u in mp[d]:
            ans[u] = dist[u] if dist[u] != float('inf') else -1

        # 以當前等級的點作為源點，更新更低等級的點
        for u in mp[d]:
            dist[u] = 0
        q = deque(mp[d])
        while q:
            u = q.popleft()
            for v in g[u]:
                if dist[u] + 1 < dist[v]:
                    dist[v] = dist[u] + 1
                    q.append(v)
  
    print(*ans)

if __name__ == "__main__":
    solve()