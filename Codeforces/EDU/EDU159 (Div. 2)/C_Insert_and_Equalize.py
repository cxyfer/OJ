from math import gcd
from collections import Counter

T = int(input())

for tc in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()

    if N == 1: # a[n+1] = 2*ai, x = ai
        print(1)
        continue

    mx, mn = max(A), min(A)
    diffs = [A[i+1] - A[i] for i in range(N-1)]
    # print(d)
    # print(A)
    # print(diff)

    cnt = Counter(diffs)
    if cnt.most_common(1)[0][1] == (N-1): # 所有的差值都相同
        # x = diff[0], a[n+1] = a[n] + x
        print((1+N) * N // 2)
        continue
    x = 0
    for dif in diffs:
        if not x:
            x = dif
        else:
            x = gcd(x, dif)
    
    ans = 0
    target = max(A)
    seen = set()
    for a in A:
        ans += (target - a) // x
        seen.add(a)
    tmp = target
    while tmp in seen:
        tmp -= x
        ans += 1
    print(ans)
    
