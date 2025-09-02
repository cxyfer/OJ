N, M = map(int, input().split(" ")) 
edges = [list(map(int, input().split(" "))) for _ in range(M)]

if M == 1:
    print(edges[0][2])
    exit()

# 對每個點DFS，紀錄最大的距離
adj = [[0]*(N+1) for _ in range(N+1)]
for edge in edges:
    X, Y, W = edge
    adj[X][Y] = W
    adj[Y][X] = W

visited = [False for _ in range(N+1)]
# ans = 0
# def dfs(v, cur=0):
#     global ans
#     visited[v] = True
#     if cur > ans:
#         ans = cur
#     for j in range(1, N+1):
#         if adj[v][j] != 0 and not visited[j]:
#             dfs(j, cur+adj[v][j])
#     visited[v] = False

# for i in range(1, N+1):
#     dfs(i, 0)
ans = 0
def dfs(v):
    cur = 0
    visited[v] = True
    for j in range(1, N+1):
        if adj[v][j] != 0 and not visited[j]:
            res = dfs(j)
            cur = max(cur, res+adj[v][j])
    visited[v] = False
    return cur 

for i in range(1, N+1):
    ans = max(ans, dfs(i))
print(ans)

exit()


disjoint_set = [i for i in range(N+1)]

def find(x):
    if disjoint_set[x] == x:
        return x
    else:
        disjoint_set[x] = find(disjoint_set[x])
        return disjoint_set[x]
    
def union(x, y):
    disjoint_set[find(x)] = find(y)

def show():
    dict = {i:[] for i in range(N+1)}
    for i in range(N+1):
        dict[find(i)].append(i) 
    return [dSet for dSet in dict.values() if dSet != []]

# Brute Force
ans = 0
for i in range(M):

    disjoint_set = [i for i in range(N+1)]
    res = [[] for i in range(N+1)] # 紀錄每個點的index
    cnt = [0 for i in range(N+1)] # 每個點只能被加入兩次
    
    cur = edges[i][2]
    cnt[edges[i][0]] += 1
    cnt[edges[i][1]] += 1
    for j in range(i+1, M):
        X, Y, W = edges[j]
        if cnt[X] < 2 and cnt[Y] < 2:
            union(X, Y)
            cnt[X] += 1
            cnt[Y] += 1
            res[X].append(j)
            res[Y].append(j)
        sets = show()
        print(sets)
        for dSet in sets:
            if len(dSet) == 1:
                continue
            tmp = 0
            ss = set([idx for idx in dSet])
            print(ss)
            for idx in dSet:
                X, Y, W = edges[idx-1]
                

       
    ans = max(ans, cur)
print(ans)
exit()

# res = [0 for i in range(N+1)]
# ans = 0

disjoint_set = [i for i in range(N+1)]

def find(x):
    if disjoint_set[x] == x:
        return x
    else:
        disjoint_set[x] = find(disjoint_set[x])
        return disjoint_set[x]
    
def union(x, y):
    disjoint_set[find(x)] = find(y)

def show():
    dict = {i:[] for i in range(N+1)}
    for i in range(N+1):
        dict[find(i)].append(i) 
    return [dSet for dSet in dict.values() if dSet != []]

# 每個點只能被加入兩次
cnt = [0 for i in range(N+1)]

ans = 0
for edge in edges:
    X, Y, W = edge
    if cnt[X] < 2 and cnt[Y] < 2:
        cnt[X] += 1
        cnt[Y] += 1
        ans += W
print(ans)

# Brute Force
ans = 0
for i in range(M):
    cnt = [0 for i in range(N+1)] # 每個點只能被加入兩次
    cur = edges[i][2]
    cnt[edges[i][0]] += 1
    cnt[edges[i][1]] += 1
    for j in range(i+1, M):
        X, Y, W = edges[j]
        if cnt[X] < 2 and cnt[Y] < 2:
            cnt[X] += 1
            cnt[Y] += 1
            cur += W
    ans = max(ans, cur)
print(ans)


