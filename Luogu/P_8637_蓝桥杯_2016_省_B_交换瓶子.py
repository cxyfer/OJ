n = int(input())
A = list(map(int, input().split()))

# 置換環
ans = n
B = sorted(range(n), key=lambda i: A[i])  # 離散化
print(B)
vis = [False] * n
for x in B:
    if vis[x]: continue
    while not vis[x]:
        vis[x] = True
        x = B[x]
    ans -= 1  # 每個環能減少一次操作
print(ans)
