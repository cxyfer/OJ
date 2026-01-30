from itertools import accumulate

def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    s = list(accumulate(A, initial=0))

    # @cache
    # def dfs(l, r):
    #     if l == r:
    #         return 0
    #     res = float('inf')
    #     for i in range(l, r):
    #         res = min(res, dfs(l, i) + dfs(i + 1, r) + s[r + 1] - s[l])
    #     return res
    # print(dfs(0, n - 1))

    f = [[float('inf')] * n for _ in range(n)]
    for l in range(n):
        f[l][l] = 0
    for ln in range(2, n + 1):
        for l in range(n - ln + 1):
            r = l + ln - 1
            f[l][r] = min(f[l][k] + f[k + 1][r] + s[r + 1] - s[l] for k in range(l, r))
    print(f[0][n - 1])

if __name__ == "__main__":
    solve()