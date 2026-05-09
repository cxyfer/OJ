def solve():
    n, m = map(int, input().split())
    s = list(map(int, input()))
    t = list(map(int, input()))
    assert len(s) == n and len(t) == m

    ans = m * 10
    for i in range(n - m + 1):
        ans = min(ans, sum((s[i + j] - t[j]) % 10 for j in range(m)))
    print(ans)


if __name__ == "__main__":
    solve()
