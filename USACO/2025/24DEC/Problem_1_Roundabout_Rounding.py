A = [45, 445, 4445, 44445, 444445, 4444445, 44444445, 444444445, 4444444445, 44444444445]
B = [49, 499, 4999, 49999, 499999, 4999999, 49999999, 499999999, 4999999999, 49999999999]

t = int(input())

for _ in range(t):
    n = int(input())

    ans = 0
    for a, b in zip(A, B):
        if n >= b:
            ans += (b - a + 1)
        else:
            ans += max(n - a + 1, 0)
            break

    print(ans)