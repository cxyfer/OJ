from math import floor, ceil

def gcd(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcd(b, a % b)
        return d, y, x - y * (a // b)

t = int(input())

for _ in range(t):
    x, k = map(int, input().split())
    a, b = floor(x / k), ceil(x / k)
    d, p, q = gcd(a, b)
    p *= x // d
    q *= x // d

    print(p, q)