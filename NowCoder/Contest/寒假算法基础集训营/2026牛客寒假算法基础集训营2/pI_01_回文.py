"""
I. 01回文
https://ac.nowcoder.com/acm/contest/120562/I

對於以某個字元為起點的回文，只需要考慮兩種情況：
1. a...a
2. ab...ba
對於其他情況，都可以被裁剪成上述兩種情況之一。

那麼我們可以將相鄰的相同字元視為一個連通分量，則：
1. 只要此連通分量內存在兩個以上相同字元，則可以構成情況 1 的回文
2. 只要與此連通分量相鄰的不同字元存在兩個以上，則可以利用相同字元作為中間部分，使這些不同字元構成回文。

然而討論完可以發現，如果一個字元要作為回文的起點，則必須存在另外一個相同字元。
又可以分成兩者相鄰和不相鄰兩種情況，然而不管哪種情況，只要存在另外一個相同字元，則可以構成回文。
因此我們只需要計算字元 0 和 1 的數量，如果其中一種字元數量 >= 2，則所有該字元都可以構成回文。
"""
import sys
from collections import deque

it = iter(sys.stdin.read().splitlines())
def input():
    return next(it)
def print(*args, sep=' ', end='\n'):
    sys.stdout.write(sep.join(map(str, args)) + end)

def solve1():
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]
     
    ans = [['N'] * m for _ in range(n)]
    vis = [[False] * m for _ in range(n)]
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if vis[i][j]:
                continue
            q = deque([(i, j)])
            vis[i][j] = True
            # 維護當前連通分量中的相同字元列表，以及與此連通分量相鄰的不同字元集合
            same, diff = list(), set()
            while q:
                r, c = q.popleft()
                same.append((r, c))
                for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
                    if 0 <= nr < n and 0 <= nc < m:
                        if grid[nr][nc] == val:
                            if vis[nr][nc]:
                                continue
                            q.append((nr, nc))
                            vis[nr][nc] = True
                        else:
                            diff.add((nr, nc))

            if len(same) >= 2:
                for x, y in same:
                    ans[x][y] = 'Y'
            if len(diff) >= 2:  # 由於是網格圖，diff 的大小最多是 4 * len(same)
                for x, y in diff:
                    ans[x][y] = 'Y'
 
    for row in ans:
        print("".join(row))

def solve2():
    n, m = map(int, input().split())
    grid = [input() for _ in range(n)]

    cnt0 = sum(row.count('0') for row in grid)
    cnt1 = n * m - cnt0

    ans = [['N'] * m for _ in range(n)]
    for i, row in enumerate(grid):
        for j, val in enumerate(row):
            if val == '0' and cnt0 >= 2 or val == '1' and cnt1 >= 2:
                ans[i][j] = 'Y'
 
    for row in ans:
        print("".join(row))

# solve = solve1
solve = solve2
 
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()