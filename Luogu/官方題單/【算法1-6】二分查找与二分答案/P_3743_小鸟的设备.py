n, p = map(int, input().split())
devices = [tuple(map(int, input().split())) for _ in range(n)]

def check(t):
    cnt = 0  # 需要補充的能量
    for a, b in devices:
        if b - a * t < 0:
            cnt += (a * t - b)
            if cnt > t * p:
                return False
    return True

left, right = 0, 1e12
while right - left > 1e-4:
    mid = (left + right) / 2
    if check(mid):
        left = mid
    else:
        right = mid
print(f"{right:.6f}" if right < 1e12 else -1)