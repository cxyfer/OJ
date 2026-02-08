"""
D. 系ぎて
https://ac.nowcoder.com/acm/contest/120563/D

題意：在網格圖上給定兩組起點與終點，判斷是否存在兩條路徑，使得兩條路徑的交集為空。

讓 A 以最短路徑連通後，檢查 B 是否仍可連通。
但只檢查 A 的最短路徑可能會錯誤地堵塞 B 的路徑，因此需要交換順序檢查一次。
.A..
B.B.
.A..
"""
from collections import deque
from typing import Optional, List, Tuple, Set

def solve():
    n, m = map(int, input().split())
    grid = [list(input().strip()) for _ in range(n)]

    pos1, pos2 = [], []
    for r, row in enumerate(grid):
        for c, ch in enumerate(row):
            if ch == '1':
                pos1.append((r, c))
            elif ch == '2':
                pos2.append((r, c))

    def bfs(st: Tuple[int, int], ed: Tuple[int, int], ch: str, banned: Set[Tuple[int, int]]) -> Optional[List[Tuple[int, int]]]:
        # 求 st 到 ed 的最短路徑，但路徑上不能有 ch，也不能經過 banned 中的點
        q = deque([st])
        prev = [[None] * m for _ in range(n)]
        prev[st[0]][st[1]] = (-1, -1)
        while q:
            r, c = q.popleft()
            if (r, c) == ed:
                break
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= nr < n and 0 <= nc < m:
                    if prev[nr][nc] is None and grid[nr][nc] != ch and (nr, nc) not in banned:
                        prev[nr][nc] = (r, c)
                        q.append((nr, nc))
        else:
            return None
        path = []
        cur = ed
        while cur != st:
            path.append(cur)
            cur = prev[cur[0]][cur[1]]
        path.append(st)
        path.reverse()
        return path

    def check(pos1: List[Tuple[int, int]], pos2: List[Tuple[int, int]], ch2: str) -> bool:
        st1, ed1 = pos1[0], pos1[1]
        st2, ed2 = pos2[0], pos2[1]

        banned = set()

        # 1. 求兩個 A 之間的最短路徑
        path1 = bfs(st1, ed1, ch2, banned)
        if path1 is None:
            return False
        banned.update(path1)

        # 2. 檢查兩個 B 之間是否仍可連通
        path2 = bfs(st2, ed2, '', banned)
        return path2 is not None

    print("YES" if check(pos1, pos2, '2') or check(pos2, pos1, '1') else "NO")

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()