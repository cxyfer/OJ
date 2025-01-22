from collections import defaultdict

S = input()
n = len(S)

pre, suf = defaultdict(int), defaultdict(int)

for i in range(n // 2):
    pre[S[i]] += 1

for i in range(n // 2, n):
    suf[S[i]] += 1

print(n - max(pre.values()) - max(suf.values()))