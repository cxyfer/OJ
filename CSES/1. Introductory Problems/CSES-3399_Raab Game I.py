t = int(input())

for _ in range(t):
    n, a, b = map(int, input().split())
    if (a == 0 and b > 0) or (b == 0 and a > 0) or (a + b == 1) or (a + b > n):
        print("NO")
        continue
    print("YES")
    A, B = [], []
    while a + b < n:
        A.append(n)
        B.append(n)
        n -= 1
    for i in range(a):
        A.append(n - i)
        B.append(a - i)
    for i in range(b):
        A.append(n - a - i)
        B.append(n - i)
    print(*A)
    print(*B)

    # cnt1 = cnt2 = 0
    # for x, y in zip(A, B):
    #     if x > y:
    #         cnt1 += 1
    #     elif x < y:
    #         cnt2 += 1
    # assert cnt1 == a and cnt2 == b
