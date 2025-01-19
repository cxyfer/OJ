from math import gcd

t = int(input())

for _ in range(t):
    x, y, a, b, c, d = map(int, input().split())
    g1, g2 = gcd(c, d), gcd(a, b)
    print("YES" if (x % g1 == 0) and (y % g2 == 0) else "NO")