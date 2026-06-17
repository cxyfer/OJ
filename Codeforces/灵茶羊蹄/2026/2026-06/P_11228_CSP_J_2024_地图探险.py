"""
P11228 [CSP-J 2024] 地图探险
https://www.luogu.com.cn/problem/P11228
"""

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solve():
    n, m, k = map(int, input().split())
    x, y, d = map(int, input().split())
    x, y = x - 1, y - 1

    R = [input().strip() for _ in range(n)]

    vis = [[False] * m for _ in range(n)]
    st = set()
    ans = 0
    while k >= 0 and (x, y, d) not in st:
        st.add((x, y, d))
        if not vis[x][y]:
            vis[x][y] = True
            ans += 1
        for dd in range(4):
            nd = (d + dd) % 4
            nx, ny = x + DIRS[nd][0], y + DIRS[nd][1]
            k -= 1
            if 0 <= nx < n and 0 <= ny < m and R[nx][ny] == ".":
                x, y = nx, ny
                d = nd
                break
        else:
            break
    print(ans)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
