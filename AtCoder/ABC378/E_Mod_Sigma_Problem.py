from atcoder.fenwicktree import FenwickTree

N, M = map(int, input().split())
A = list(map(int, input().split()))

s = [0] * (N + 1)
for i, x in enumerate(A):
    s[i+1] = (s[i] + x) % M

bit = FenwickTree(M)
bit.add(0, 1)

ans = 0
s_sl = 0 # sum(s[l])
for r in range(1, N+1):
    # 以 r 為右端點的區間有 r 個，其和為 s[r] * r - sum(s[l])
    ans += s[r] * r - s_sl
    # 計算有多少個 l 滿足 s[l] % MOD > s[r] % MOD，即逆序對數量
    # 對於這種情況，由於取模後不會是負數，所以需要補加 M 回來
    ans += M * (r - bit.sum(0, s[r] + 1)) 
    bit.add(s[r], 1)
    s_sl += s[r]
print(ans)