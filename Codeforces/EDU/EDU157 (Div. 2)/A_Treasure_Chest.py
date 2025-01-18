t = int(input())
for ts in range(t):
    x, y, k = map(int, input().split())
    if (y < x):
        print(x)
    else:
        pos = x+k # 寶箱可以被移動到的位置
        if (pos > y):
            print(y)
        else:
            print(pos + (y-pos) * 2)