from math import inf


def solve():
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == N

    ans = inf
    for x in A:
        m = (T + x - 1) // x  # ceil(T / x)
        ans = min(ans, x * m)
    print(ans)


if __name__ == "__main__":
    solve()
