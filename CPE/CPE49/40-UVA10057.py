while True:
    try:
        n = int(input())
        A = [int(input()) for _ in range(n)]
    except EOFError:
        break
    A.sort()
    x = A[n//2] if n & 1 else A[n//2-1]
    if n & 1:
        y = sum([a == x for a in A])
    else:
        y = sum([a == A[n//2-1] or a == A[n//2] for a in A])
    z = 1 if n & 1 else A[n//2] - A[n//2-1] + 1
    print(x, y, z)