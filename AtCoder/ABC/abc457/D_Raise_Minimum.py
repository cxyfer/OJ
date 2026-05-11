def solve():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))

    def check(mid: int) -> bool:
        left_k = k
        for i, x in enumerate(A, start=1):
            if x >= mid:
                continue
            # 使用 math.ceil 會有浮點數誤差
            # left_k -= math.ceil((mid - x) / i)
            left_k -= ((mid - x) + i - 1) // i
            if left_k < 0:
                return False
        return True

    left = min(A)
    right = min(x + i * k for i, x in enumerate(A, start=1))
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            left = mid + 1
        else:
            right = mid - 1
    print(right)


if __name__ == "__main__":
    solve()
