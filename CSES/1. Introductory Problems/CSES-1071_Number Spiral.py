t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    if x < y:
        if y & 1: # y % 2 == 1
            print(y * y - x + 1)
        else:
            print((y - 1) * (y - 1) + x)
    else:
        if x & 1: # x % 2 == 1
            print((x - 1) * (x - 1) + y)
        else:
            print(x * x - y + 1)