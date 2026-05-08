def solve():
    n = int(input())
    A = list(map(int, input().split()))

    A.sort(reverse=True)

    print(sum(A[i] for i in range(0, n, 2)) - sum(A[i] for i in range(1, n, 2)))


if __name__ == "__main__":
    solve()
