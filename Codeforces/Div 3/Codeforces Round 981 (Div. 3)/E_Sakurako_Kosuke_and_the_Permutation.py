"""
    置換環
"""

t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    vis = [False] * n
    ans = 0
    for x in range(n):
        if vis[x]: continue
        length = 0
        while not vis[x]:
            vis[x] = True
            x = p[x] - 1
            length += 1
        if length >= 3:
            ans += (length - 1) // 2
    print(ans)