"""
    Math (Horner's Rule)
    a_0 * x^n + a_1 * x^(n-1) + ... + a_(n-1) * x + a_n
    欲求 a_0 * n * x^(n-1) + a_1 * (n-1) * x^(n-2) + ... + a_(n-2) * 2 * x + a_(n-1)
    一直提出 x 
"""
while True:
    try:
        x = int(input())
        A = list(map(int, input().split()))
    except EOFError:
        break
    n = len(A) - 1
    # ans = A[0] * n 
    # for i in range(1, n):
    #     ans = ans * x + A[i] * (n - i)
    ans = 0
    for i, a in enumerate(A[:-1]):
        ans = ans * x + a * (n - i)
    print(ans)