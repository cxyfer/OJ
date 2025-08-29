"""
2136B - Like the Bitset
https://codeforces.com/contest/2136/problem/B
構造

如果有連續 k 個 1，則需滿足 A[i] > A[i+k-1] 及 A[i+k-1] > A[i]，此時無法構造；
否則可以把 1 的位置放較小的數字，0 的位置放較大的數字。
"""
from itertools import groupby

def solve():
    n, k = map(int, input().split())
    s = input()

    for ch, l in groupby(s):
        if ch == '1' and len(list(l)) >= k:
            print("NO")
            return
    print("YES")

    ans = [-1] * n
    x = 1
    for i, ch in enumerate(s):
        if ch == '1':
            ans[i] = x
            x += 1
    for i in range(n):
        if ans[i] == -1:
            ans[i] = x
            x += 1
    print(*ans)

t = int(input())
for _ in range(t):
    solve()