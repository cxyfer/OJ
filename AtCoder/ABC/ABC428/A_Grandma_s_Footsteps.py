def solve():
    S, A, B, X = map(int, input().split())

    q, r = divmod(X, A + B)
    ans = (q * A + min(r, A)) * S
    print(ans)


if __name__ == "__main__":
    solve()
