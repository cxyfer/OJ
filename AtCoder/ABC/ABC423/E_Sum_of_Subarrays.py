from itertools import accumulate

def solve():
    N, Q = map(int, input().split())
    A = list(map(int, input().split()))

    s0 = list(accumulate(A, initial=0))
    s1 = list(accumulate([i * x for i, x in enumerate(A, start=1)], initial=0))
    s2 = list(accumulate([i * i * x for i, x in enumerate(A, start=1)], initial=0))

    for _ in range(Q):
        L, R = map(int, input().split())
        ans = 0
        ans += -1 * (s2[R] - s2[L - 1])
        ans += (L + R) * (s1[R] - s1[L - 1])
        ans += (-L + 1) * (R + 1) * (s0[R] - s0[L - 1])
        print(ans)

if __name__ == "__main__":
    solve()