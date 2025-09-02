N = int(input())
Ds  = [list(map(int, input().split(" "))) for _ in range(N-1)]

# 1. 將D轉換成Adjacency Matrix
adj = [[0]*(N) for _ in range(N)]
for i, row in enumerate(Ds):
    for j, val in enumerate(row):
        adj[i][j+i+1] = val
        adj[j+i+1][i] = val
# for i in range(N):
#     for j in range(N):
#         print(adj[i][j], end=" ")
#     print()

visited = [False] * N
# DFS
def DFS(i):
    visited[i] = True
    for j in range(N):
        if adj[i][j] == 1 and not visited[j]:
            DFS(j)

