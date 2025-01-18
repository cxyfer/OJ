a, b, c, d = map(float, input().split())

def f(x):
    return a * x ** 3 + b * x ** 2 + c * x + d

ans = []
for left in range(-100, 100):
    right = left + 1

    fl, fr = f(left), f(right)
    if fl == 0:
        ans.append(left)
        continue

    if fl * fr >= 0:
        continue

    if fl < 0:  # 遞增
        while right - left > 1e-4:
            mid = (left + right) / 2
            if f(mid) < 0:  # 根在 mid 右側
                left = mid
            else:
                right = mid
    else:  # 遞減
        while right - left > 1e-4:
            mid = (left + right) / 2
            if f(mid) > 0:  # 根在 mid 右側
                left = mid
            else:
                right = mid
    ans.append(left)

print(*map(lambda x: f"{x:.2f}", ans))