"""
    二分圖判斷：DFS / BFS / Disjoint Set
    https://zhuanlan.zhihu.com/p/161082172
    賽間寫DFS的時候用忘了把color也放進去stack了
"""
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

g = [[] for _ in range(N+1)] # N node from 1 to N
for i in range(M):
    if A[i] == B[i]:
        print("No")
        exit()
    u, v = A[i], B[i]
    g[u].append(v)
    g[v].append(u)

colors = [0] * (N+1) # 0: not colored, 1/-1: colored

for u in range(1, N+1):
    if colors[u] == 0:
        stack = [(u, 1)] # (node, color)
        colors[u] = 1
        while stack:
            u, color = stack.pop()
            for v in g[u]:
                if colors[v] == 0: # not colored
                    stack.append((v, -color))
                    colors[v] = -color
                elif colors[v] == color:
                    print("No")
                    exit()
print("Yes")