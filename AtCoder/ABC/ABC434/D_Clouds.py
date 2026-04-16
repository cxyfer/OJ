H = W = 2000


def solve():
    N = int(input())
    clouds = [tuple(map(int, input().split())) for _ in range(N)]

    # 二維差分維護每個格子被覆蓋的次數
    grid1 = [[0] * (W + 2) for _ in range(H + 2)]
    for x1, x2, y1, y2 in clouds:
        grid1[x1][y1] += 1
        grid1[x2 + 1][y2 + 1] += 1
        grid1[x1][y2 + 1] -= 1
        grid1[x2 + 1][y1] -= 1
    for i in range(1, H + 2):
        for j in range(1, W + 2):
            grid1[i][j] += grid1[i - 1][j] + grid1[i][j - 1] - grid1[i - 1][j - 1]

    tot0 = 0
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            tot0 += grid1[i][j] == 0

    # 對恰好被覆蓋一次的格子數做二維前綴和
    grid2 = [[0] * (W + 2) for _ in range(H + 2)]
    for i in range(1, H + 1):
        for j in range(1, W + 1):
            grid2[i][j] = (
                grid2[i - 1][j]
                + grid2[i][j - 1]
                - grid2[i - 1][j - 1]
                + (grid1[i][j] == 1)
            )

    # 移除某朵雲會減少覆蓋數量為二維區間中恰好被覆蓋一次的格子數
    ans = []
    for x1, x2, y1, y2 in clouds:
        cur = tot0 + (
            grid2[x2][y2]
            - grid2[x1 - 1][y2]
            - grid2[x2][y1 - 1]
            + grid2[x1 - 1][y1 - 1]
        )
        ans.append(cur)
    print(*ans, sep="\n")


if __name__ == "__main__":
    solve()
