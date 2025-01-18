import sys
input = sys.stdin.readline
def print(val=""): sys.stdout.write(str(val) + "\n")

kase = 1
anses = []
while True:
    n = int(input())
    if n == 0:
        break
    M = [tuple(map(int, input().split())) for _ in range(n)]
    P = [M[0][0]]
    for a, b in M:
        P.append(b)
    
    f = [[float("inf")] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        f[i][i] = 0
    
    for ln in range(2, n + 1):
        for i in range(1, n - ln + 2):
            j = i + ln - 1
            for k in range(i, j):
                t = f[i][k] + f[k + 1][j] + P[i - 1] * P[k] * P[j]
                if t < f[i][j]:
                    f[i][j] = t
                    s[i][j] = k
    
    def build(i, j):
        if i == j:
            return f"A{i}"
        k = s[i][j]
        left = build(i, k)
        right = build(k + 1, j)
        return f"({left} x {right})"

    ans = build(1, n)
    # print(f"Case {kase}: {ans}")
    anses.append(f"Case {kase}: {ans}")
    kase += 1

print("\n".join(anses))