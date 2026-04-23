"""
P2216 [HAOI2007] 理想的正方形
https://www.luogu.com.cn/problem/P2216
Monotonic Queue

二維版本的 239. Sliding Window Maximum
可以先對橫列(row)做一次 Sliding Window Maximum，得到 n * (m - k + 1) 的矩陣
再對新矩陣的直行(col)做一次 Sliding Window Maximum，得到 (n - k + 1) * (m - k + 1) 的矩陣
"""

from collections import deque


def solve():
    n, m, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    assert len(grid) == n and len(grid[0]) == m

    mx1 = [[0] * (m - k + 1) for _ in range(n)]
    mn1 = [[0] * (m - k + 1) for _ in range(n)]

    for i, row in enumerate(grid):
        q1 = deque()
        q2 = deque()
        for j, x in enumerate(row):
            while q1 and row[q1[-1]] <= x:
                q1.pop()
            while q2 and row[q2[-1]] >= x:
                q2.pop()
            q1.append(j)
            q2.append(j)
            while q1 and q1[0] <= j - k:
                q1.popleft()
            while q2 and q2[0] <= j - k:
                q2.popleft()
            if j >= k - 1:
                mx1[i][j - k + 1] = row[q1[0]]
                mn1[i][j - k + 1] = row[q2[0]]

    mx2 = [[0] * (m - k + 1) for _ in range(n - k + 1)]
    for j, col in enumerate(zip(*mx1)):
        q = deque()
        for i, x in enumerate(col):
            while q and col[q[-1]] <= x:
                q.pop()
            q.append(i)
            while q and q[0] <= i - k:
                q.popleft()
            if i >= k - 1:
                mx2[i - k + 1][j] = col[q[0]]

    mn2 = [[0] * (m - k + 1) for _ in range(n - k + 1)]
    for j, col in enumerate(zip(*mn1)):
        q = deque()
        for i, x in enumerate(col):
            while q and col[q[-1]] >= x:
                q.pop()
            q.append(i)
            while q and q[0] <= i - k:
                q.popleft()
            if i >= k - 1:
                mn2[i - k + 1][j] = col[q[0]]

    ans = float("inf")
    for row1, row2 in zip(mx2, mn2):
        for a, b in zip(row1, row2):
            ans = min(ans, a - b)
    print(ans)


if __name__ == "__main__":
    solve()
