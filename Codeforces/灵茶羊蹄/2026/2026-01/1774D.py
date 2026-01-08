def solve():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    cnt = [sum(row) for row in grid]
    tot = sum(cnt)
    if tot % n:
        print(-1)
        return -1
    avg = tot // n

    ops = []
    for j in range(m):
        arr1 = []
        arr2 = []
        for i in range(n):
            if grid[i][j] == 1 and cnt[i] > avg:
                arr1.append(i)
            elif grid[i][j] == 0 and cnt[i] < avg:
                arr2.append(i)
        for i1, i2 in zip(arr1, arr2):
            ops.append((i1 + 1, i2 + 1, j + 1))
            grid[i1][j] = 0
            grid[i2][j] = 1
            cnt[i1] -= 1
            cnt[i2] += 1
    
    print(len(ops))
    for i1, i2, j in ops:
        print(i1, i2, j)
    assert all(sum(row) == avg for row in grid)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()