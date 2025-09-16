from math import gcd, comb

def solve():
    N, M, Y = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort()
    S = [0] * (N + 1)

    def dfs(i: int, cnt: int, l: int) -> None:
        if i == N:
            S[cnt] += Y // l
            return
        if l > Y:
            return
        dfs(i + 1, cnt, l)
        x = A[i]
        g = gcd(l, x)
        dfs(i + 1, cnt + 1, l * x // g)

    dfs(0, 0, 1)
    ans = 0
    for k in range(M, N + 1):
        if ((k - M) & 1) == 0:
            ans += comb(k, M) * S[k]
        else:
            ans -= comb(k, M) * S[k]
    print(ans)

if __name__ == "__main__":
    solve()