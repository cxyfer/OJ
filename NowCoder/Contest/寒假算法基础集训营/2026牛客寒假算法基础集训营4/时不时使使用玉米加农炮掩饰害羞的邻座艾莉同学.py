"""
H. 时不时使使用玉米加农炮掩饰害羞的邻座艾莉同学
https://ac.nowcoder.com/acm/contest/120564/H

注意到每次修改後，最多只會影響 5x5 範圍內的 13 個位置，
因此可以暴力更新這 13 個位置的得分，並使用懶刪除堆維護最大得分位置。
然而由於更新只加不減，因此也可以只檢查是否有新的最大得分位置出現即可。
"""
from heapq import heappush, heappop

def solve1():
    n, m, q = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    dirs = [(dr, dc) for dr in range(-2, 3) for dc in range(-2, 3) if abs(dr) + abs(dc) <= 2]
    scores = [[0] * m for _ in range(n)]
    for r, row in enumerate(grid):
        for c, v in enumerate(row):
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    scores[nr][nc] += v

    hp = []
    for r, row in enumerate(scores):
        for c, v in enumerate(row):
            heappush(hp, (-v, r, c))

    for _ in range(q):
        x, y, z = map(int, input().split())
        x -= 1
        y -= 1
        
        for dr, dc in dirs:
            nr, nc = x + dr, y + dc
            if 0 <= nr < n and 0 <= nc < m:
                scores[nr][nc] += z
                heappush(hp, (-scores[nr][nc], nr, nc))

        # 懶刪除堆，刪除「貨不對版」的最大值
        while hp and -hp[0][0] != scores[hp[0][1]][hp[0][2]]:
            heappop(hp)

        _, r, c = hp[0]
        print(r + 1, c + 1)

def solve2():
    n, m, q = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    dirs = [(dr, dc) for dr in range(-2, 3) for dc in range(-2, 3) if abs(dr) + abs(dc) <= 2]
    scores = [[0] * m for _ in range(n)]
    for r, row in enumerate(grid):
        for c, v in enumerate(row):
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    scores[nr][nc] += v

    ans = (0, 0)
    for r, row in enumerate(scores):
        for c, v in enumerate(row):
            if v > scores[ans[0]][ans[1]]:
                ans = (r, c)

    for _ in range(q):
        x, y, z = map(int, input().split())
        x -= 1
        y -= 1
        
        for dr, dc in dirs:
            nr, nc = x + dr, y + dc
            if 0 <= nr < n and 0 <= nc < m:
                scores[nr][nc] += z
                if scores[nr][nc] > scores[ans[0]][ans[1]]:
                    ans = (nr, nc)

        print(ans[0] + 1, ans[1] + 1)

# solve = solve1
solve = solve2

if __name__ == "__main__":
    solve()