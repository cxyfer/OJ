def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    assert len(A) == n

    def check(mid: int) -> bool:
        cnt = 0
        s = 0
        for x in A:
            if s + x > mid:
                cnt += 1
                s = 0
            s += x
        if s > 0:
            cnt += 1
        return cnt <= k

    left, right = max(A), sum(A)
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            right = mid - 1
        else:
            left = mid + 1
    print(left)


if __name__ == "__main__":
    solve()
