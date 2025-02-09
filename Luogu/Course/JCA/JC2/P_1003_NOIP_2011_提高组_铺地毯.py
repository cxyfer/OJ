n = int(input().strip())

carpets = [tuple(map(int, input().strip().split())) for _ in range(n)]

x, y = map(int, input().strip().split())

for i in range(n - 1, -1, -1):
    a, b, g, k = carpets[i]
    if a <= x <= a + g and b <= y <= b + k:
        print(i + 1)
        break
else:
    print(-1)