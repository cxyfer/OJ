def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    s = 0
    for i, x in enumerate(A, start=1):
        s += x
        if s >= k:
            print(i)
            break
    else:
        print(-1)


if __name__ == "__main__":
    solve()
