from math import gcd
from itertools import pairwise

t = int(input())

for _ in range(t):
    n = int(input())
    A = list(map(int, input().split()))

    B = [0] * (n - 1)
    for i, (x, y) in enumerate(pairwise(A)):
        B[i] = gcd(x, y)

    pre = [True] * n
    suf = [True] * n
    for i in range(1, n - 1):
        pre[i] = pre[i - 1] and B[i - 1] <= B[i]
    for i in range(n - 2, 0, -1):
        suf[i] = suf[i + 1] and B[i - 1] <= B[i]

    # 可以刪 A[0] 或 A[n-1]
    if pre[n - 3] or suf[2]:
        print("YES")
        continue
    
    # 枚舉刪除的元素
    flag = False
    for i in range(1, n - 1):
        x = A[i]
        # 會少 B[i-1] = gcd(A[i-1], A[i]) 和 B[i] = gcd(A[i], A[i+1])
        # 但會多 gcd(A[i-1], A[i+1])
        g = gcd(A[i - 1], A[i + 1])

        b_prev = B[i - 2] if i - 2 >= 0 else 0
        b_next = B[i + 1] if i + 1 < n - 1 else float('inf')

        if pre[max(i - 2, 0)] and suf[min(i + 2, n - 1)] and b_prev <= g <= b_next:
            print("YES")
            break
    else:
        print("NO")