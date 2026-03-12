from itertools import accumulate


def solve():
    N, M, K, T = map(int, input().split())
    B = list(map(int, input().split()))

    A = [0] * N
    for b in B:
        A[b - 1] = 1
    s = list(accumulate(A, initial=0))

    ans = []
    for _ in range(K):
        L, R = map(int, input().split())
        ans.append("YES" if s[R] - s[L - 1] >= T else "NO")
    print(*ans, sep="\n")


if __name__ == "__main__":
    solve()
