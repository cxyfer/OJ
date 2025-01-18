n, m = map(int, input().split())
edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u - 1, v - 1, w))

# Bellman-Ford
dist = [0] * n
prev = [-1] * n
for _ in range(n): # 這裡要多跑一次，因為可能會有負環
    flag = False # 是否還能找到可以鬆弛的邊
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            prev[v] = u
            last = v
            flag = True
    if not flag:
        print("NO")
        exit()

# 找到負環
print("YES")
for i in range(n): # 走 n 步回到環上
    last = prev[last]
cycle = [last]
t = prev[last]
while t != last:
    cycle.append(t)
    t = prev[t]
cycle.append(t)
cycle.reverse()
print(*map(lambda x: x + 1, cycle))