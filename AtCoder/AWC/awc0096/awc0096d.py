def solve():
    n = int(input())
    D = list(map(int, input().split()))
    assert len(D) == n

    h0 = h1 = 0
    for d in D:
        h0 = max(h0 + d, 0)
        h1 = max(h1 + d, 0)
        h1 = min(h1, h0 // 2)
    print(h1)


if __name__ == "__main__":
    solve()
