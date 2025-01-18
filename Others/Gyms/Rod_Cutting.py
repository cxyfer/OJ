n = int(input())
P = [0] + list(map(int, input().split()))

f = [-float("inf")] * (n + 1)
f[0] = 0
for i in range(1, n + 1):
    f[i] = max(P[j] + f[i - j] for j in range(i + 1))
print(f[n])