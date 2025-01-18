"""
    Catalan Number + 因子計數法

    C(2n, n) / (2n + 1)
    = (2n)! / (n! * n! * (n + 1))
    = [(n + 1) * (n + 2) * ... * (2n)] / [n! * (n + 1)]
    = [(n + 2) * ... * (2n)] / n!
"""
n, p = map(int, input().split())

MAXN = 2 * n
minpf = [0] * (MAXN + 1) # 最小質因數
for i in range(2, MAXN + 1):
    if minpf[i] == 0:
        for j in range(i * 2, MAXN + 1, i):
            if minpf[j] == 0:
                minpf[j] = i

# cnt = [0] * (MAXN + 1)
# for i in range(2, n + 1):
#     cnt[i] = -1
# for i in range(n + 2, MAXN + 1):
#     cnt[i] = 1
cnt = [0] * 2 + [-1] * (n - 1) + [0] + [1] * (n - 1)

for i in range(2 * n, 1, -1):
    if minpf[i] != 0:
        cnt[minpf[i]] += cnt[i]
        cnt[i // minpf[i]] += cnt[i]
        cnt[i] = 0

ans = 1
for i in range(2, 2 * n + 1):
    if cnt[i] != 0:
        ans = ans * pow(i, cnt[i], p) % p
print(ans)
