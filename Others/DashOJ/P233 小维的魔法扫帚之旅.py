d, k, a, b, t = map(int, input().split())

ans = d * b  # 全部徒步
for m in [1, d // k - 1, d // k, d // k + 1]:
    ans = min(ans, min(d, m * k) * a + (m - 1) * t + (d - min(d, m * k)) * b)
print(ans)