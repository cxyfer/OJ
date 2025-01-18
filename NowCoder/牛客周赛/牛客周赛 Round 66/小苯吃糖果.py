a, b, c = map(int, input().split())
mx = max(a, b, c)
print(max(mx, a + b + c - mx))