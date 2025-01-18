from itertools import accumulate

t = int(input())
for _ in range(t):
    n, m, v = map(int, input().split())
    A = list(map(int, input().split()))
    s = list(accumulate(A, initial=0))

    lc = [0] * (n + 1)
    last = 0
    for i in range(1, n + 1):
        if s[i] - s[last] >= v:
            lc[i] = lc[last] + 1
            last = i
        else:
            lc[i] = lc[i - 1]

    rc = [0] * (n + 2)
    last = n + 1
    for i in range(n, 0, -1):
        if s[last - 1] - s[i - 1] >= v:
            rc[i] = rc[last] + 1
            last = i
        else:
            rc[i] = rc[i + 1]

    def check(mid):
        if mid == 0:
            if lc[n] >= m:
                return True
        else:
            l = 0
            for r in range(1, n+1):
                while l < r and s[r] - s[l] >= mid:
                    if lc[l] + rc[r+1] >= m:
                        return True
                    l += 1
        return False

    left = 0
    right = s[n]
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            ans = mid
            left = mid + 1
        else:
            right = mid - 1

    if right > 0 or (right == 0 and lc[n] >= m):
        print(right)
    else:
        print(-1)