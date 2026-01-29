def solve():
    n = int(input())
    A = list(map(int, input().split()))

    # @cache
    # def dfs(l: int, r: int) -> int:
    #     if l > r:
    #         return 0
    #     v = l + (n - 1 - r)
    #     if v & 1 == 0:
    #         return max(dfs(l + 1, r) + A[l], dfs(l, r - 1) + A[r])
    #     else:
    #         return min(dfs(l + 1, r) - A[l], dfs(l, r - 1) - A[r])
    # print(dfs(0, n - 1))

    f = [[0] * n for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i, n):
            v = i + (n - 1 - j)
            f1 = f[i + 1][j] if i < n - 1 else 0
            f2 = f[i][j - 1] if j > 0 else 0
            if v & 1 == 0:
                f[i][j] = max(f1 + A[i], f2 + A[j])
            else:
                f[i][j] = min(f1 - A[i], f2 - A[j])
    print(f[0][n - 1])

if __name__ == "__main__":
    solve()