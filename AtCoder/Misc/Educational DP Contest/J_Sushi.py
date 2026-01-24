"""
dfs(i, j, k) 表示當前有 i 個 1 個盤子，j 個 2 個盤子，k 個 3 個盤子時，最後一個盤子的期望值
dfs(i, j, k) = (n - i - j - k) / n * dfs(i, j, k) + i/n * dfs(i-1, j, k) + j/n * dfs(i+1, j-1, k) + k/n * dfs(i, j+1, k-1) + 1
整理得:
dfs(i, j, k) = (n + i * dfs(i-1, j, k) + j * dfs(i+1, j-1, k) + k * dfs(i, j+1, k-1)) / (i + j + k)
"""
def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    cnt = [0] * 4
    for a in A:
        cnt[a] += 1

    f = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
    # for k in range(n + 1):
    #     for j in range(n - k + 1):
    #         for i in range(n - k - j + 1):
    s1 = cnt[1] + cnt[2] + cnt[3]
    s2 = cnt[2] + cnt[3]
    for k in range(cnt[3] + 1):
        for j in range(min(s2, n - k) + 1):
            for i in range(min(s1, n - k - j) + 1):
                if i == 0 and j == 0 and k == 0:
                    continue
                v = n
                if i > 0:
                    v += i * f[i-1][j][k]
                if j > 0:
                    v += j * f[i+1][j-1][k]
                if k > 0:
                    v += k * f[i][j+1][k-1]
                f[i][j][k] = v / (i + j + k)
    print(f[cnt[1]][cnt[2]][cnt[3]])

if __name__ == "__main__":
    solve()