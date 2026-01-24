def solve():
    s = input().strip()
    t = input().strip()
    n, m = len(s), len(t)

    f = [[0] * (m + 1) for _ in range(n + 1)]
    for i, c1 in enumerate(s, start=1):
        for j, c2 in enumerate(t, start=1):
            if c1 == c2:
                f[i][j] = f[i - 1][j - 1] + 1
            else:
                f[i][j] = max(f[i - 1][j], f[i][j - 1])

    i, j = n, m
    ans = []
    while i > 0 and j > 0:
        if s[i - 1] == t[j - 1]:
            ans.append(s[i - 1])
            i, j = i - 1, j - 1
        else:
            if f[i - 1][j] >= f[i][j - 1]:
                i -= 1
            else:
                j -= 1
    print(''.join(reversed(ans)))
    
if __name__ == "__main__":
    solve()