t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))
    s = 0
    for i in range(1, n, 2):
        s ^= A[i]
    print("first" if s != 0 else "second")