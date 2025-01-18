MOD = 998244353
N, M = map(int, input().split(" "))
edges = [ list(map(int, input().split(" "))) for _ in range(M) ]


G = [[1]*N for _ in range(N)]
for i in range(N):
    G[i][i] = 0
for i in range(M):
    u, v = edges[i]
    G[u-1][v-1] = float('inf')
    G[v-1][u-1] = float('inf')
def Dijkstra(G, start):
    start -= 1
    inf = float('inf')
    node_num = N
    visited = [0] * node_num
    dis = {node: G[start][node] for node in range(node_num)}
    parents = {node: -1 for node in range(node_num)}
    visited[start] = 1
    last_point = start

    for i in range(node_num - 1):
        min_dis = inf
        for j in range(node_num):
            if visited[j] == 0 and dis[j] < min_dis:
                min_dis = dis[j]
                last_point = j
        visited[last_point] = 1
        if i == 0:
            parents[last_point] = start + 1
        for k in range(node_num):
            if G[last_point][k] < inf and dis[k] > dis[last_point] + G[last_point][k]:
                dis[k] = dis[last_point] + G[last_point][k]
                parents[k] = last_point + 1

    return {key+1: values for key, values in dis.items()}, {key + 1: values for key, values in parents.items()}

dis, parents = Dijkstra(G, 1)
print(dis[N] % MOD) if dis[N] != float('inf') else print(-1)