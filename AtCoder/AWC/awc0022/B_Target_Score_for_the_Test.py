def solve():
    N, M, T = map(int, input().split())
    A = list(map(int, input().split()))

    ans = sum(max(T - x, 0) for x in A)
    print(ans if ans <= M else -1)


if __name__ == "__main__":
    solve()
