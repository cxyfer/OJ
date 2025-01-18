from collections import defaultdict
t = int(input())

def bar(x):
    res = 0
    for i in range(31):
        if not x & (1 << i):
            res |= (1 << i)
    return res

for _ in range(t):
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    cnt = defaultdict(int)
    ans = N
    for x in A:
        if cnt[str(bar(x))] > 0:
            ans -= 1
            cnt[str(bar(x))] -= 1
        else:
            cnt[str(x)] += 1
    print(ans)