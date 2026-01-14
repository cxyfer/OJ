def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    ans = 0
    for i, x in enumerate(A):
        s = x
        for j in range(i + 1, n):
            s += A[j]
            if all(s % A[k] != 0 for k in range(i, j + 1)):
                ans += 1
    print(ans)

if __name__ == "__main__":
    solve()