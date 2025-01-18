t = int(input())
for _ in range(t):
    a, b = map(list, input().split())
    a[0], b[0] = b[0], a[0]
    print(''.join(a), ''.join(b))