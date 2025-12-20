from bisect import bisect_right
from itertools import accumulate

MOD = 998244353

def solve():
    n, m = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    assert len(A) == n and len(B) == m

    B.sort()
    sb = list(accumulate(B, initial=0))

    ans = 0
    for x in A:
        idx = bisect_right(B, x)
        ans += idx * x - sb[idx]
        ans += sb[m] - sb[idx] - (m - idx) * x
        ans %= MOD
    print(ans)

if __name__ == "__main__":
    solve()