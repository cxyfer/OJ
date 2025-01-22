t = int(input())

for _ in range(t):
    n, k = map(int, input().split())

    if k == 1:
        print(n)
        continue
    # if k >= 60:
    if k > 60:
        print(1)
        continue

    def check(n, k, m):
        res = 1
        while k > 0:
            if k & 1:
                res = res * m
                if res > n:
                    return False
            k = k >> 1
            m = m * m
        return True
    
    left, right = 1, min(n, int(1e18))
    while left <= right:
        mid = (left + right) // 2
        if check(n, k, mid):
            left = mid + 1
        else:
            right = mid - 1

    ans = max(1, right)
    print(ans if abs(n - pow(ans, k)) <= abs(pow(ans + 1, k) - n) else ans + 1)