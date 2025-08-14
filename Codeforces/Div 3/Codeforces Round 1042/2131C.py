"""
x => y
1. (y - x) = ak
2. (y - (k - (x % k)) = bk

(y - x) = ak => y % k = x % k
"""
from collections import defaultdict

t = int(input())

def solve():
    n, k = map(int, input().split())
    S = list(map(int, input().split()))
    T = list(map(int, input().split()))

    cnt1, cnt2 = defaultdict(int), defaultdict(int)
    for x in S:
        cnt1[str(x % k)] += 1
    for y in T:
        cnt2[str(y % k)] += 1

    for i in cnt1.keys() | cnt2.keys():
        if cnt1[i] + cnt1[str((k - int(i)) % k)] != cnt2[i] + cnt2[str((k - int(i)) % k)]:
            print("NO")
            return
    print("YES")

for _ in range(t):
    solve()