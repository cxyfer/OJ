def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    print(sum(A) + (n - 1) // k)


if __name__ == "__main__":
    solve()
