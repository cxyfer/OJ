"""
P3501 [POI 2010] ANT-Antisymmetry
https://www.luogu.com.cn/problem/P3501
String Hashing + Binary Search / Manacher

求 XOR 意義下的迴文字串數量
"""
from random import randint

n = int(input())
s = input()
t = ''.join(str(int(c) ^ 1) for c in s)

MOD = 1070777777
BASE = randint(int(1e8), int(1e9))

P = [1] + [0] * n
H1, H2 = [0] * (n + 1), [0] * (n + 1)
for i in range(n):
    P[i + 1] = P[i] * BASE % MOD
for i, b in enumerate(s, 1):
    H1[i] = (H1[i - 1] * BASE + ord(b)) % MOD
for i in range(n - 1, -1, -1):
    H2[i] = (H2[i + 1] * BASE + ord(t[i])) % MOD

ans = 0
for r in range(1, n):
    l = r - 1
    left, right = 0, min(r, n - r)
    while left <= right:
        mid = (left + right) // 2
        # s[l-mid+1..l]
        hs1 = (H1[l + 1] - H1[l + 1 - mid] * P[mid]) % MOD
        # t[r...r+mid-1]
        hs2 = (H2[r] - H2[r + mid] * P[mid]) % MOD
        if hs1 == hs2:
            left = mid + 1
        else:
            right = mid - 1
    ans += right

print(ans)