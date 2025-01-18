from itertools import accumulate

n = int(input())
A = list(map(int, input().split()))

# s[i] = sum(A[:i])
s = list(accumulate(A, initial=0))

# f[i][j] stores minimum cost for interval [i,j]
f = [[0] * n for _ in range(n)]
# m[i][j] stores optimal split point for interval [i,j]
m = [[0] * n for _ in range(n)]

# Initialize base cases
for i in range(n):
    m[i][i] = i

for ln in range(2, n + 1):
    for i in range(n - ln + 1):
        j = i + ln - 1
        f[i][j] = float('inf')
        tot = s[j + 1] - s[i]

        # Use Knuth's optimization
        # Search for k in [m[i][j-1], m[i+1][j]]
        left = m[i][j - 1]
        right = min(m[i + 1][j], j - 1)
        for k in range(left, right + 1):
            val = f[i][k] + f[k + 1][j] + tot
            if val < f[i][j]:
                f[i][j] = val
                m[i][j] = k

# Build expression and collect costs
costs = []
def build(i, j):
    if i == j:
        return str(A[i])
    k = m[i][j]
    left = build(i, k)
    right = build(k + 1, j)
    costs.append(s[j + 1] - s[i])
    return f"({left}+{right})"

print(build(0, n-1))
print(f[0][n-1])
print(*costs)