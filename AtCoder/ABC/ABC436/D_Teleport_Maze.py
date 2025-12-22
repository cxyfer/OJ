from collections import deque, defaultdict

def solve():
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]

    # 預處理：記錄每種字母的所有出現位置
    pos = defaultdict(list)
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch.isalpha():
                pos[ch].append((r, c))

    vis = [[False] * W for _ in range(H)]
    vis[0][0] = True
    q = deque([(0, 0, 0)])  # (dist, r, c)
    while q:
        d, r, c = q.popleft()
        if r == H - 1 and c == W - 1:
            print(d)
            return

        # 1. 上下左右移動
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= nr < H and 0 <= nc < W and grid[nr][nc] != '#' and not vis[nr][nc]:
                vis[nr][nc] = True
                q.append((d + 1, nr, nc))
        
        # 2. 傳送移動
        ch = grid[r][c]
        if ch.isalpha() and pos[ch]:
            for nr, nc in pos[ch]:
                if not vis[nr][nc]:
                    vis[nr][nc] = True
                    q.append((d + 1, nr, nc))
            # 關鍵：清空該字母的列表，避免重複處理
            pos[ch].clear()
    print(-1)

if __name__ == "__main__":
    solve()