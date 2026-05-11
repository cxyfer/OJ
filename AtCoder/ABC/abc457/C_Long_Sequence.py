def solve():
    n, k = map(int, input().split())

    A = [list(map(int, input().split()))[1:] for _ in range(n)]
    C = list(map(int, input().split()))

    for i, (c, lst) in enumerate(zip(C, A)):
        m = len(lst)
        if k > c * m:
            k -= c * m
            continue
        print(lst[(k - 1) % m])
        break


if __name__ == "__main__":
    solve()
