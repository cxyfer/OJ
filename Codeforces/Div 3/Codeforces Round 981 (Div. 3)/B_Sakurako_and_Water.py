"""
    貪心
    注意到增加高度是沒有副作用的，因此每次需要增加時，都可以盡可能的使用最大範圍。
    而每次增加的位置為對角線，因此可以維護該對角線的增加次數。
"""

t = int(input())

for _ in range(t):
    n = int(input())
    M = [list(map(int, input().split())) for _ in range(n)]

    d = [0] * (2 * n + 1)
    for i, row in enumerate(M):
        for j, val in enumerate(row):
            c = i - j + n # 對角線，做了偏移
            if val + d[c] < 0: # 還需要增加
                d[c] = -val
    print(sum(d))