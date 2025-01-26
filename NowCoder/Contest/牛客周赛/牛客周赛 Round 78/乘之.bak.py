t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    ans = sum(A)
    D = [x * (k - 1) for x in A]

    print(D)
    mx_v = -float('inf')
    mx = (0, 0)
    s = s_mn = 0
    s_mn_idx = -1
    for i, x in enumerate(D):
        s += x
        if s - s_mn > mx_v:
            mx_v = s - s_mn
            mx = (s_mn_idx + 1, i)
        if s < s_mn:
            s_mn = s
            s_mn_idx = i
    print(mx)  
    for i in range(mx[0], mx[1] + 1):
        ans += D[i]
        D[i] = 0

    mn_v = float('inf')
    mn = (0, 0)
    s = s_mx = 0
    s_mx_idx = -1
    for i, x in enumerate(D):
        s += x
        if s - s_mx < mn_v:
            mn_v = s - s_mx
            mn = (s_mx_idx + 1, i)
        if s > s_mx:
            s_mx = s
            s_mx_idx = i
    print(mn)
    for i in range(mn[0], mn[1] + 1):
        ans += D[i]
        D[i] = 0

    print(ans)