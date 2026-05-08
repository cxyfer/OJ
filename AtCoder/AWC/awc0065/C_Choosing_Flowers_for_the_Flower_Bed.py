def solve():
    n = int(input())
    A = list(map(int, input().split()))

    f = [0] * (n + 2)
    for i, x in enumerate(A, start=2):
        f[i] = max(f[i - 1], f[i - 2] + x)
    print(max(f))


if __name__ == "__main__":
    solve()
