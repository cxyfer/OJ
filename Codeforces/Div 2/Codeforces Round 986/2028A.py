DIR = {
    'N': (0, 1),
    'E': (1, 0),
    'S': (0, -1),
    'W': (-1, 0)
}

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    s = input()
    m = len(s)

    x, y = 0, 0
    i = 0
    while i < 1000:
        ch = s[i % m]
        dx, dy = DIR[ch]
        x += dx
        y += dy
        i += 1
        if x == a and y == b:
            print("YES")
            break
    else:
        print("NO")