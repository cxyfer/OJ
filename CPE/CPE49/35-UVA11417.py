from math import gcd

while True:
    N = int(input())
    if N == 0:
        break
    ans = 0
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            ans += gcd(i, j)
    print(ans)