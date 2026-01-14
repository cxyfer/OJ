def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    i = r = 0
    while i <= min(r, n - 1):
        r = max(r, i + A[i] - 1)
        i += 1
    print(i)

if __name__ == "__main__":
    solve()