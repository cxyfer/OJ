t = int(input())

for _ in range(t):
    a1, a2, a4, a5 = map(int, input().split())
    A = [a1, a2, -1, a4, a5]

    def count():
        return sum(A[i - 1] + A[i - 2] == A[i] for i in range(2, 5))

    ans = 0
    A[2] = a1 + a2
    ans = max(ans, count())
    A[2] = a4 - a2
    ans = max(ans, count())
    A[2] = a5 - a4
    ans = max(ans, count())
    print(ans)