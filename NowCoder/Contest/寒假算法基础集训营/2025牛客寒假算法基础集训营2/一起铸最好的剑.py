from math import floor, log

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    if m == 1:
        print(1)
        continue

    k = floor(log(n) / log(m))
    if abs(pow(m, k) - n) <= abs(pow(m, k + 1) - n):
        print(max(1, k))
    else:
        print(max(1, k + 1))