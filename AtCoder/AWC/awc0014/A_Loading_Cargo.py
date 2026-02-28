def solve():
    n, r, t = map(int, input().split())
    P = list(map(int, input().split()))

    print(*(min(t // p, r) for p in P))


if __name__ == "__main__":
    solve()
