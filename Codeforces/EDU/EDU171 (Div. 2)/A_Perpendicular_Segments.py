"""
    (0, 0) 到 (X, Y) 的區域內，選擇兩條互相垂直的線段，且兩條線段的長度都至少為 K

    (0, 0) 到 (m, m) 的對角線即為最長的線段
"""
t = int(input())

for _ in range(t):

    X, Y, K = map(int, input().split())

    m = min(X, Y)

    print(0, 0, m, m)
    print(0, m, m, 0)