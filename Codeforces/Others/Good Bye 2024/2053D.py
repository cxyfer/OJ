from bisect import bisect_right

MOD = 998244353

def solve():
    n, q = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    assert len(A) == n and len(B) == n

    sl1 = sorted(A)
    sl2 = sorted(B)

    prod = 1
    for x, y in zip(sl1, sl2):
        prod = (prod * min(x, y)) % MOD
    ans = [prod]
    for _ in range(q):
        o, x = map(int, input().split())
        x -= 1
        if o == 1:
            idx = bisect_right(sl1, A[x]) - 1
            if sl1[idx] < sl2[idx]:
                prod = (prod * pow(A[x], MOD - 2, MOD)) % MOD
                prod = (prod * (A[x] + 1)) % MOD
            sl1[idx] += 1
            A[x] += 1
        else:
            idx = bisect_right(sl2, B[x]) - 1
            if sl2[idx] < sl1[idx]:
                prod = (prod * pow(B[x], -1, MOD)) % MOD
                prod = (prod * (B[x] + 1)) % MOD
            sl2[idx] += 1
            B[x] += 1
        ans.append(prod)
    print(*ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()