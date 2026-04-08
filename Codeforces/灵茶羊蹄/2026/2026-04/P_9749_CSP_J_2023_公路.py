import math


def solve():
    n, d = map(int, input().split())
    V = list(map(int, input().split()))
    A = list(map(int, input().split()))
    assert len(V) == n - 1 and len(A) == n

    ans = r = 0
    mn = float("inf")
    for v, a in zip(V, A):
        mn = min(mn, a)
        v -= r
        q = math.ceil(v / d)
        ans += q * mn
        r = q * d - v
    print(ans)


if __name__ == "__main__":
    solve()
