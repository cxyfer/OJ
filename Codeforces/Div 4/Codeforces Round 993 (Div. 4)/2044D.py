t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    ans = [-1] * n
    vis = [False] * (n + 1)
    idx = 1

    for i, x in enumerate(A):
        if vis[x]:
            while vis[idx]:
                idx += 1
            ans[i] = idx
            vis[idx] = True
        else:
            ans[i] = x
            vis[x] = True
    print(*ans)