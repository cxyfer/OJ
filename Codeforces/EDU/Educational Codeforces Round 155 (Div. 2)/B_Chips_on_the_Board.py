t = int(input())
for tc in range(t):
    N = int(input())
    A = list(map(int, input().split(" ")))
    B = list(map(int, input().split(" ")))

    s1 = min(A) * N + sum(B)
    s2 = min(B) * N + sum(A)
    print(min(s1, s2))