t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    
    s = 0
    l, r = n, -1
    for i, x in enumerate(A):
        s += x
        if x % k != 0:
            l = min(l, i)
            r = i

    if s % k != 0:
        print(n)
    elif r == -1:
        print(-1)
    else:
        print(max(r, n - 1 - l))