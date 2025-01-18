t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    if y < x: x, y = y, x
    print(x, y)