mp = "ACGT" # in lexicographical order
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = ""
    err = 0
    for j in range(m):
        cnt = [0] * 4
        for i in range(n):
            cnt[mp.index(s[i][j])] += 1
        mx = max(cnt)
        ans += mp[cnt.index(mx)]
        err += n - mx
    print(ans)
    print(err)