"""
顯然有一部份的 col 會選擇上面，有另一部份的 col 會選擇下面，且恰有 1 個 col 同時選擇上面和下面
基於貪心思路，每個 col 選擇都先選擇較大的部分，即 max(col[0][i], col[1][i])
而剩下的較小的部分 min(col[0][i], col[1][i])，則只能在 n 個 col 中選擇 1 個，因此維護其最大的較小值
"""
t = int(input())

for _ in range(t):
    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(2)]

    s = 0
    k = -float('inf')
    for j in range(n):
        s += max(grid[0][j], grid[1][j]) # 先選擇較大的部分
        k = max(k, min(grid[0][j], grid[1][j])) # 維護最大的較小值
    print(s + k)