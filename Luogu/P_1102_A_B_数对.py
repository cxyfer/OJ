"""
A − B = C => A = B + C / B = A - C
枚舉 B 則計算 B + C 的數量：枚舉 A 則計算 A - C 的數量
"""
from collections import defaultdict

N, C = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
cnt = defaultdict(int)
for x in A:
    cnt[x] += 1
for x in A:
    ans += cnt[x - C] # 本題 x - C / x + C 都可以
print(ans)