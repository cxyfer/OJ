from bisect import *

N, X = map(int, input().split())
foods = [[] for _ in range(3)]
for _ in range(N):
    v, a, c = map(int, input().split())
    foods[v - 1].append((a, c))

# f[v][j] 表示當花費 j 元時，可以獲得的最大維生素量
f = [[0] * (X + 1) for _ in range(3)]
for v, foods_v in enumerate(foods):
    for a, c in foods_v:
        for j in range(X, -1, -1):
            if j - c < 0:
                break
            f[v][j] = max(f[v][j], f[v][j - c] + a)

def check(k):
    return sum(bisect_left(f[v], k) for v in range(3)) <= X

left, right = 0, int(1e12)
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        left = mid + 1
    else:
        right = mid - 1
print(right)