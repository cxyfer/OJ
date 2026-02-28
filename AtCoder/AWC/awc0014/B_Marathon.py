def solve():
    n, v = map(int, input().split())
    D = list(map(int, input().split()))
    T = list(map(int, input().split()))

    ans = []
    s = 0
    for i, (d, t2) in enumerate(zip(D, T), start=2):
        s += d
        t1 = s / v
        if t1 < t2:
            ans.append(i)

    print(*ans) if ans else print(-1)


if __name__ == "__main__":
    solve()
