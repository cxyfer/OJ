SHIFT = int(1e3)
MAX_V = int(2e3)


def main():
    n, m = map(int, input().split())

    # 曼哈頓距離透過旋轉後轉換成歐幾里得距離求解
    grid = [[0] * (MAX_V + 2) for _ in range(MAX_V + 2)]
    for _ in range(n):
        x, y, c = map(int, input().split())
        u = x + y
        v = x - y + SHIFT
        grid[u + 1][v + 1] += c

    for i in range(1, MAX_V + 2):
        for j in range(1, MAX_V + 2):
            grid[i][j] += grid[i - 1][j] + grid[i][j - 1] - grid[i - 1][j - 1]

    ans = []
    for _ in range(m):
        x, y, k = map(int, input().split())
        u, v = x + y, x - y + SHIFT

        u1 = max(u - k, 0) + 1
        u2 = min(u + k, MAX_V) + 1
        v1 = max(v - k, 0) + 1
        v2 = min(v + k, MAX_V) + 1

        ans.append(
            grid[u2][v2] - grid[u1 - 1][v2] - grid[u2][v1 - 1] + grid[u1 - 1][v1 - 1]
        )

    print(*ans, sep="\n")


if __name__ == "__main__":
    main()
