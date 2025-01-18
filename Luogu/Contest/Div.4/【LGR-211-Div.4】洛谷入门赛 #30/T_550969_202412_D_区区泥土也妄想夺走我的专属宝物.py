n = int(input())

for _ in range(n):
    a, *X = map(int, input().split())
    print(f"{X.count(0) / a:.10f}")
