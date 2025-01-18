from math import sqrt
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    s = sum(A)
    if int(sqrt(s)) ** 2 == s:
        print('YES')
    else:
        print('NO')