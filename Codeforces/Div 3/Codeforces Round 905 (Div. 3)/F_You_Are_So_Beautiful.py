"""
左端點是左起第一次出現的元素，右端點是右起第一次出現的元素。
"""
from collections import defaultdict

T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    cnt1 = defaultdict(int)
    f = [0] * N
    for i, a in enumerate(A):
        cnt1[a] += 1
        if cnt1[a] == 1:
            f[i] = 1

    cnt2 = defaultdict(int)
    num = 0
    ans = 0
    for i in range(N - 1, -1, -1):
        cnt2[A[i]] += 1
        if cnt2[A[i]] == 1:
            num += 1
        if f[i]:
            ans += num
    print(ans)
