"""
    AC: UVA, CPE, ZeroJudge
"""
T = int(input())

def check(x, y, r):
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    for i in range(-r, r + 1):
        for j in range(-r, r + 1):
            if x + i < 0 or x + i >= M or y + j < 0 or y + j >= N:
                return False
            if mp[x + i][y + j] != mp[x][y]:
                return False
    return True

for _ in range(T):
    M, N, Q = map(int, input().split())
    mp = [list(input()) for _ in range(M)]
    print(M, N, Q)
    for _ in range(Q):
        qx, qy = map(int, input().split())
        left, right = 0, min(M, N)
        while left <= right:
            mid = (left + right) // 2
            if check(qx, qy, mid):
                left = mid + 1
            else:
                right = mid - 1
        print(2 * right + 1)