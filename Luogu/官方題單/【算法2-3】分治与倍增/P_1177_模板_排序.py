def solve():
    n = int(input())
    A = list(map(int, input().split()))
    assert len(A) == n

    # A.sort()
    # print(*A)

    # Merge Sort
    tmp = [0] * n

    def dfs(l: int, r: int) -> None:
        if l == r:
            return
        mid = (l + r) // 2
        dfs(l, mid)
        dfs(mid + 1, r)

        i, j = l, mid + 1
        k = l
        while k <= r:
            if j > r or (i <= mid and A[i] < A[j]):
                tmp[k] = A[i]
                i += 1
            else:
                tmp[k] = A[j]
                j += 1
            k += 1

        for i in range(l, r + 1):
            A[i] = tmp[i]

    dfs(0, n - 1)
    print(*A)


if __name__ == "__main__":
    solve()
