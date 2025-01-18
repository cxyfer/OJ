from math import comb

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    ans = 1
    while N:
        x = N % 10
        ans *= comb(x+2, 2)
        N //= 10
    print(ans)