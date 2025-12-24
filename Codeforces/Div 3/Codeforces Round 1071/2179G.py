def query(i, j):
    print(f"? {i} {j}", flush=True)
    return int(input())

def answer(ans: list[list[int]]):
    print("!", flush=True)
    for row in ans:
        print(*row, flush=True)

def solve():
    n = int(input())
    m = n * n

    # 隨便指定一點，網格中與其最遠的點必為角落的點 (類似兩次 DFS/BFS 求樹上直徑)
    u = 1
    dist1 = [0] * (m + 1)
    for v in range(1, m + 1):
        d = query(u, v) if v != u else 0
        dist1[v] = d

    # x 為角落上的一點，求其到所有點的距離
    x = max(range(1, m + 1), key=lambda v: dist1[v])
    distx = [0] * (m + 1)
    for v in range(1, m + 1):
        distx[v] = query(x, v) if v != x else 0

    # 與 x 距離為 n - 1 的點可以構成一條對角線，用類似前述的方式找出對角線上兩端的點 y
    cands = [v for v in range(1, m + 1) if distx[v] == n - 1]
    y = max(cands, key=lambda v: query(cands[0], v) if v != cands[0] else 0)

    disty = [0] * (m + 1)
    for v in range(1, m + 1):
        disty[v] = query(y, v) if v != y else 0

    # 此時找到了相鄰的兩個角落點 x 和 y
    # 不妨設 x = (1, 1), y = (1, n)，其他點的座標可以透過距離計算得出。
    grid = [[-1] * n for _ in range(n)]
    for v in range(1, m + 1):
        dx, dy = distx[v], disty[v]
        r = (dx + dy - n + 3) // 2
        c = (dx - dy + n + 1) // 2
        grid[r - 1][c - 1] = v
    answer(grid)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()