N = int(input())

d = [[] for _ in range(4)]
for _ in range(N):
    x, y = map(int, input().split())
    ty = (x + y) & 1
    d[ty * 2].append(x + y)
    d[ty * 2 + 1].append(x - y)

ans = 0
for di in d:
    di.sort()
    n = len(di)
    for i in range(n):
        ans += (i * 2 - n + 1) * di[i]
print(ans // 2)