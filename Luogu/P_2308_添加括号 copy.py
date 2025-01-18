from itertools import accumulate

n = int(input())
A = list(map(int, input().split()))

s = list(accumulate(A, initial=0))
f = [[0] * n for _ in range(n)]
opt = [[0] * n for _ in range(n)]

for i in range(n):
    opt[i][i] = i

for ln in range(2, n + 1):
    for i in range(n - ln + 1):
        j = i + ln - 1
        f[i][j] = float('inf')
        tot = s[j + 1] - s[i]
        start = opt[i][j - 1]
        end = opt[i + 1][j] if (i + 1) <= j else j - 1
        end = min(end, j - 1)
        for k in range(start, end + 1):
            val = f[i][k] + f[k + 1][j] + tot
            if val < f[i][j]:
                f[i][j] = val
                opt[i][j] = k

costs = []
def build(i, j):
    if i == j:
        return str(A[i])
    k = opt[i][j]
    left = build(i, k)
    right = build(k + 1, j)
    costs.append(s[j + 1] - s[i])
    return f"({left}+{right})"

print(build(0, n - 1))
print(f[0][n - 1])
print(*costs)