"""
    Meet in the Middle
"""
from collections import Counter

n, x = map(int, input().split())
A = list(map(int, input().split()))

n1, n2 = n // 2, n - n // 2
s1 = []
for i in range(n1):
    s1 = s1 + [s + A[i] for s in s1] + [A[i]]
cnt1 = Counter(s1)

s2 = []
for i in range(n1, n):
    s2 = s2 + [s + A[i] for s in s2] + [A[i]]
cnt2 = Counter(s2)
# 計算兩邊的組合數
ans = 0
for k, v in cnt1.items():
    ans += v * cnt2[x - k]
ans += cnt1[x] + cnt2[x] # 只選一邊的組合數
print(ans)