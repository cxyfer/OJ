def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    x = int(input())
    print(A[x - 1])


if __name__ == "__main__":
    solve()
