def solve():
    n, q = map(int, input().split())
    A = list(map(lambda x: int(x) - 1, input().split()))

    pos = [[0] * 32 for _ in range(n)]
    val = [[0] * 32 for _ in range(n)]

    for i, x in enumerate(A):
        pos[i][0] = x
        val[i][0] = i + 1

    for j in range(1, 32):
        for i in range(n):
            pos[i][j] = pos[pos[i][j - 1]][j - 1]
            val[i][j] = val[i][j - 1] + val[pos[i][j - 1]][j - 1]

    for _ in range(q):
        t, b = map(int, input().split())
        b -= 1
        ans = 0
        for i in range(32):
            if (t >> i) & 1:
                ans += val[b][i]
                b = pos[b][i]
        print(ans)


if __name__ == "__main__":
    solve()
