while True:
    n, m = map(int, input().strip().split())
    if n == 0 and m == 0:
        break
    heads = [int(input().strip()) for _ in range(n)]
    knights = [int(input().strip()) for _ in range(m)]
    heads.sort()
    knights.sort()
    ans = 0
    i = 0
    for head in heads:
        while i < m and knights[i] < head:
            i += 1
        if i == m:
            ans = 'Loowater is doomed!'
            break
        ans += knights[i]
        i += 1
    print(ans)