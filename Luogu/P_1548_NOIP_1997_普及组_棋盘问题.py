from math import comb

n, m = map(int, input().split())

tot = comb(n + 1, 2) * comb(m + 1, 2)
k = min(n, m)
s2 = 0
for i in range(1, k + 1):
    s2 += (n - i + 1) * (m - i + 1)

print(s2, tot - s2)