"""
Warnsdorff’s algorithm
"""

N = 8
MOVES = [(2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), (-2, -1), (-1, -2)]

y, x = map(lambda x: int(x) - 1, input().split())
grid = [[0] * N for _ in range(N)]

def isValid(x, y):
    return x >= 0 and x < N and y >= 0 and y < N and grid[x][y] == 0

def getMovesCnt(x, y):
    return sum(isValid(x + dx, y + dy) for dx, dy in MOVES)

def dfs(x, y, idx):
    grid[x][y] = idx
    if idx == N * N:
        for line in grid:
            print(*line)
        exit(0)

    moves = []
    for i, (dx, dy) in enumerate(MOVES):
        nx, ny = x + dx, y + dy
        if isValid(nx, ny):
            moves.append((getMovesCnt(nx, ny), (nx, ny)))
    moves.sort(key=lambda x: x[0])
    for _, (nx, ny) in moves:
        dfs(nx, ny, idx + 1)
        grid[nx][ny] = 0

dfs(x, y, 1)