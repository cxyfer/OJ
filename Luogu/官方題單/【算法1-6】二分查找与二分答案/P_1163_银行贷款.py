w0, w, m = map(int, input().split())

def check(x):
    cnt = 0
    for i in range(1, m + 1):
        cnt += w * pow(1 / (1 + x), i)  # 每個月的實際環款金額
    return cnt >= w0

left, right = 0, 3
while right - left > 1e-4:
    mid = (left + right) / 2
    if check(mid):
        left = mid
    else:
        right = mid

print(f"{round(left * 100, 1):.1f}")