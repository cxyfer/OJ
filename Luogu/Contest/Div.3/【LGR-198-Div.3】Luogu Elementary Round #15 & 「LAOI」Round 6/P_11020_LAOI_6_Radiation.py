t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    sz = min(n, m)
    r = max(0, k - sz)
    ans = []
    for i in range(n):
        cur = ""
        for j in range(m):
            if i == j and k:
                cur += 'S'
                k -= 1
            elif r:
                cur += 'S'
                r -= 1
            else:
                cur += '.'
        ans.append(cur)
    print(*ans, sep='\n')