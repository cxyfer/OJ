def solve():
    n = int(input())
    grid = [list(map(int, input().split()))[1:] for _ in range(n)]

    x, y = map(int, input().split())
    print(grid[x - 1][y - 1])


if __name__ == "__main__":
    solve()
